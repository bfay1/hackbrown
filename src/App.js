import { useState, useEffect } from 'react';
import axios from "axios";
import YoutubeEmbed from "./youtubeembed"
import { TypeWriter } from 'react-simple-typewriter';
import './App.css';

function App() {

  const [id, setId] = useState(null);
  const [err, setError] = useState(true);
  const [question, setQuestion] = useState('');
  const [typeQuestion, setTypeQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [ansLoading, setAnsLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/${id}/`);
        setId(response.data.id);
      } catch (err) {
         setError(err);
         alert(err);
      } finally {
        setGetLoading(false);
      }
    };
    fetchData();
  }, []);
  
  const sendQuestion = async (e) => {
    e.preventDefault();
    setAnsLoading(true);
    setTypeQuestion(`Question: ${question}`);
    try {
      const response = await axios.post(`http://localhost:5000/${id}/`, {"question" : question});
      setAnswer(`Answer: ${response.data.message}`);
    } catch (err) {
      alert('Error sending question: ' + err);
    } finally {
      setAnsLoading(false);
      setQuestion('');
    }
  };

  return (
    <div className='flex flex-col justify-start items-center p-5 h-screen bg-black'>
      <div className='flex flex-row justify-around items-center p-5 my-5 rounded-lg w-full bg-gray-500'>
        {!getLoading && <YoutubeEmbed embedId={id}/>}
        <div className='flex flex-col w-1/2 justify-between items-center h-full ml-5'>
          <div className='flex w-full rounded-lg p-3 bg-gray-200 h-1/4 overflow-y-auto'>{typeQuestion}</div>
          <div className='flex w-full rounded-lg p-3 bg-gray-200 h-2/3 overflow-y-auto'>
            {ansLoading ? <div>hold on, let me think...</div> : (answer && <TypeWriter typeSpeed={30} words={[answer]}/>)}
          </div>
        </div>
      </div>
      <form onSubmit={sendQuestion} className='flex justify-between w-full'>
        <input value={question} type='text' placeholder='Ask a question...' onChange={(e) => setQuestion(e.target.value)} className='bg-gray-200 p-2 rounded-lg w-full' />
      </form>
    </div>
  );
}

export default App;
