// server.js
const express = require('express');
const cors = require('cors');
const fs = require('fs').promises;
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Helper function to read file content
const readFileContent = async (filePath) => {
  try {
    const content = await fs.readFile(filePath, 'utf8');
    return content;
  } catch (error) {
    // Gracefully handle file not found, otherwise throw
    if (error.code === 'ENOENT') {
      return null;
    }
    throw new Error(`Failed to read file: ${error.message}`);
  }
};

// Helper function to parse question metadata from question.py
const parseQuestionMetadata = (content) => {
  if (!content) return { questionNumber: null, title: null, fullContent: content };

  const lines = content.split('\n');
  let questionNumber = null;
  let title = 'Untitled';

  for (const line of lines) {
    if (line.includes('Question Number:')) {
      questionNumber = line.split('Question Number:')[1]?.trim() || null;
    }
    if (line.includes('Title:')) {
      title = line.split('Title:')[1]?.trim() || 'Untitled';
    }
  }
  
  return { questionNumber, title, fullContent: content };
};

// Route to get all questions metadata
app.get('/api/questions', async (req, res) => {
  try {
    const problemsDir = path.join(__dirname, 'problems');
    const folders = await fs.readdir(problemsDir);
    
    const questionPromises = folders
      .filter(folder => folder.startsWith('Question'))
      .map(async (folder) => {
        const questionPath = path.join(problemsDir, folder, 'question.py');
        const questionContent = await readFileContent(questionPath);
        const metadata = parseQuestionMetadata(questionContent);
        
        // **MODIFICATION: Filter out question #0 and invalid questions**
        if (metadata.questionNumber && metadata.questionNumber !== '0') {
          return {
            number: metadata.questionNumber.padStart(3, '0'),
            title: metadata.title,
            folder: folder
          };
        }
        return null;
      });

    const questionsMetadata = (await Promise.all(questionPromises)).filter(Boolean);
    
    // Sort by question number
    questionsMetadata.sort((a, b) => parseInt(a.number, 10) - parseInt(b.number, 10));
    
    res.json(questionsMetadata);
  } catch (error) {
    console.error('Error getting questions:', error);
    res.status(500).json({ error: 'Failed to fetch questions' });
  }
});

// Route to get a specific question by folder name
app.get('/api/questions/:folder', async (req, res) => {
  try {
    const { folder } = req.params;
    const questionPath = path.join(__dirname, 'problems', folder, 'question.py');
    const answerPath = path.join(__dirname, 'problems', folder, 'answer.py');
    
    const questionContent = await readFileContent(questionPath);
    if (!questionContent) {
        return res.status(404).json({ error: 'Question not found' });
    }
    
    const metadata = parseQuestionMetadata(questionContent);
    const answerContent = await readFileContent(answerPath);
    
    res.json({
      number: metadata.questionNumber,
      title: metadata.title,
      folder: folder,
      question: {
        fullContent: metadata.fullContent,
      },
      answer: answerContent || 'No solution available.'
    });
    
  } catch (error) {
    console.error('Error getting question:', error);
    res.status(404).json({ error: 'Question not found' });
  }
});

// Route to get question by question number
app.get('/api/questions/number/:number', async (req, res) => {
  // **MODIFICATION: Immediately reject requests for #0 or #000**
  const { number } = req.params;
  if (parseInt(number, 10) === 0) {
      return res.status(404).json({ error: 'Question not found' });
  }

  try {
    const problemsDir = path.join(__dirname, 'problems');
    const folders = await fs.readdir(problemsDir);
    
    let targetFolder = null;
    
    for (const folder of folders) {
      if (folder.startsWith('Question')) {
        const questionPath = path.join(problemsDir, folder, 'question.py');
        const questionContent = await readFileContent(questionPath);
        const metadata = parseQuestionMetadata(questionContent);
        
        if (metadata.questionNumber === number) {
          targetFolder = folder;
          break;
        }
      }
    }
    
    if (!targetFolder) {
      return res.status(404).json({ error: 'Question not found' });
    }
    
    // Redirect to the folder-based route to avoid code duplication
    res.redirect(307, `/api/questions/${targetFolder}`);
    
  } catch (error) {
    console.error('Error getting question by number:', error);
    res.status(500).json({ error: 'Failed to fetch question' });
  }
});

// Health check route
app.get('/api/health', (req, res) => {
  res.json({ status: 'Server is running', timestamp: new Date().toISOString() });
});

// 404 handler for any other route
app.use('*', (req, res) => {
  res.status(404).json({ error: `Route not found: ${req.originalUrl}` });
});

// Central error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/api/health`);
  console.log(`Questions API: http://localhost:${PORT}/api/questions`);
});

module.exports = app;