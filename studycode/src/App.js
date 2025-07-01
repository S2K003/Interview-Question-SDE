import React, { useState, useEffect } from 'react';
import { Menu, X, ChevronRight, Code, FileText, Hash } from 'lucide-react';

const LeetCodeClone = () => {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch all questions on component mount
  useEffect(() => {
    fetchQuestions();
  }, []);

  // Load first question when questions are fetched
  useEffect(() => {
    if (questions.length > 0 && !currentQuestion) {
      loadQuestion(questions[0].folder);
    }
  }, [questions, currentQuestion]);

  const fetchQuestions = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/questions');
      if (!response.ok) throw new Error('Failed to fetch questions');
      const data = await response.json();
      setQuestions(data);
    } catch (err) {
      setError('Failed to load questions');
      console.error('Error fetching questions:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadQuestion = async (folder) => {
    try {
      const response = await fetch(`http://localhost:5000/api/questions/${folder}`);
      if (!response.ok) throw new Error('Failed to fetch question');
      const data = await response.json();
      setCurrentQuestion(data);
      setIsMenuOpen(false); // Close menu after selection
    } catch (err) {
      setError('Failed to load question');
      console.error('Error loading question:', err);
    }
  };

  // ## MODIFICATION IS HERE ##
  // This function now returns the content directly without segregation.
  const formatQuestionContent = (content) => {
    return content || '';
  };

  const formatAnswerContent = (content) => {
    if (!content) return 'No solution available';
    
    // Remove docstrings and format Python code
    const lines = content.split('\n');
    let formattedCode = '';
    let inDocstring = false;
    
    for (const line of lines) {
      if (line.includes('"""')) {
        inDocstring = !inDocstring;
        if (!inDocstring) continue;
        if (inDocstring && line.trim() !== '"""') {
          formattedCode += `# ${line.replace('"""', '').trim()}\n`;
        }
      } else if (!inDocstring) {
        formattedCode += line + '\n';
      } else {
        formattedCode += `# ${line.trim()}\n`;
      }
    }
    
    return formattedCode;
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="glass-card p-8 rounded-2xl flex flex-col items-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-white"></div>
          <p className="text-white mt-4">Loading questions...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-900 relative overflow-hidden">
      {/* Background decorative elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-gray-500 rounded-full mix-blend-overlay filter blur-xl opacity-10 animate-pulse"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-gray-500 rounded-full mix-blend-overlay filter blur-xl opacity-10 animate-pulse delay-1000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-gray-500 rounded-full mix-blend-overlay filter blur-xl opacity-10 animate-pulse delay-500"></div>
      </div>

      {/* Header */}
      <header className="relative z-50 p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="glass-card p-3 rounded-xl hover:bg-white/20 transition-all duration-300 hover:scale-105"
            >
              {isMenuOpen ? (
                <X className="w-6 h-6 text-white" />
              ) : (
                <Menu className="w-6 h-6 text-white" />
              )}
            </button>
            <h1 className="text-2xl font-bold text-white">
              LeetCode Clone
            </h1>
          </div>
          
          {currentQuestion && (
            <div className="glass-card px-4 py-2 rounded-xl">
              <span className="text-gray-300 text-sm">Question #{currentQuestion.number}</span>
            </div>
          )}
        </div>
      </header>

      {/* Sidebar Menu */}
      <div className={`fixed top-0 left-0 h-full w-80 bg-gray-950/70 backdrop-blur-xl z-40 transform transition-transform duration-300 ${
        isMenuOpen ? 'translate-x-0' : '-translate-x-full'
      }`}>
        <div className="p-6 pt-20">
          <h2 className="text-xl font-semibold text-white mb-6 flex items-center">
            <Hash className="w-5 h-5 mr-2" />
            All Questions
          </h2>
          
          <div className="space-y-3 max-h-[calc(100vh-200px)] overflow-y-auto custom-scrollbar">
            {questions.map((question) => (
              <button
                key={question.folder}
                onClick={() => loadQuestion(question.folder)}
                className={`w-full text-left p-4 rounded-xl transition-all duration-300 hover:scale-105 group ${
                  currentQuestion?.folder === question.folder
                    ? 'glass-card-active'
                    : 'glass-card hover:bg-white/10'
                }`}
              >
                <div className="flex items-center justify-between">
                  <div>
                    <div className="text-sm text-gray-400 mb-1">#{question.number}</div>
                    <div className="text-white font-medium group-hover:text-gray-100 transition-colors">
                      {question.title}
                    </div>
                  </div>
                  <ChevronRight className="w-4 h-4 text-gray-500 group-hover:text-gray-200 transition-colors" />
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Main Content */}
      <main className="relative z-10 p-4 pt-0">
        {error && (
          <div className="glass-card p-4 rounded-xl mb-4 border border-gray-600/30">
            <p className="text-gray-300">{error}</p>
          </div>
        )}

        {currentQuestion ? (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-[calc(100vh-120px)]">
            {/* Question Panel */}
            <div className="glass-card p-6 rounded-2xl overflow-hidden flex flex-col">
              <div className="flex items-center mb-4">
                <FileText className="w-5 h-5 text-gray-300 mr-2" />
                <h2 className="text-xl font-semibold text-white">
                  {currentQuestion.title}
                </h2>
              </div>
              
              <div className="flex-1 overflow-y-auto custom-scrollbar">
                {/* The 'prose' class is removed to avoid automatic formatting */}
                <div className="max-w-none">
                  <pre className="text-gray-300 text-sm leading-relaxed whitespace-pre-wrap font-mono">
                    {formatQuestionContent(currentQuestion.question.fullContent)}
                  </pre>
                </div>
              </div>
            </div>

            {/* Answer Panel */}
            <div className="glass-card p-6 rounded-2xl overflow-hidden flex flex-col">
              <div className="flex items-center mb-4">
                <Code className="w-5 h-5 text-gray-300 mr-2" />
                <h2 className="text-xl font-semibold text-white">Solution</h2>
              </div>
              
              <div className="flex-1 overflow-y-auto custom-scrollbar">
                <pre className="text-gray-200 text-sm leading-relaxed font-mono bg-gray-800/60 p-4 rounded-xl">
                  <code>{formatAnswerContent(currentQuestion.answer)}</code>
                </pre>
              </div>
            </div>
          </div>
        ) : (
          <div className="flex items-center justify-center h-[calc(100vh-120px)]">
            <div className="glass-card p-8 rounded-2xl text-center">
              <FileText className="w-16 h-16 text-white/40 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-white mb-2">No Question Selected</h3>
              <p className="text-white/60">Select a question from the menu to get started</p>
            </div>
          </div>
        )}
      </main>

      {/* Overlay for mobile menu */}
      {isMenuOpen && (
        <div
          className="fixed inset-0 bg-gray-950/60 z-30 lg:hidden"
          onClick={() => setIsMenuOpen(false)}
        ></div>
      )}

      <style jsx>{`
        .glass-card {
          background: rgba(255, 255, 255, 0.05);
          backdrop-filter: blur(20px);
          border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .glass-card-active {
          background: rgba(255, 255, 255, 0.15);
          backdrop-filter: blur(20px);
          border: 1px solid rgba(255, 255, 255, 0.25);
        }
        
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.05);
          border-radius: 3px;
        }
        
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.2);
          border-radius: 3px;
        }
        
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.4);
        }
      `}</style>
    </div>
  );
};

export default LeetCodeClone;