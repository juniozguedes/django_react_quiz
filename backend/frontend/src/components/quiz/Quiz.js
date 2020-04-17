import React, { useState, useEffect } from 'react';
import api from '../../api'

// import { Container } from './styles';

export default function Quiz() {
    const [questions, setQuestions] = useState([])
 
    useEffect(() => {
        async function loadQuestions(){
            const response = await api.get('questions/all')
            setQuestions(response.data);
        }
        loadQuestions();
    }, [])

    function handleAnswer(e,event){
        console.log(e)
        console.log(event.target.innerHTML)
        if (e[0].choice === event.target.innerHTML){
            console.log('right')
            console.log(event)
        }
        else{
            console.log('nope')
        }
    }
  return (
    <div>
        <div className="questionCard">
            <h1>Pergunta:</h1>
        </div>
        <div className="choiceCard">
            <ul>
                {questions.map((question) => (
                    <div key={question.question}>
                        <h1>{question.question}</h1>
                        {question.choices.map((choice)=>(
                            <ul key={choice.choice}>
                                <button onClick={() => handleAnswer(question.correct, event)}>{choice.choice}</button>
                            </ul>
                        ))}
                    </div>
                ))}
            </ul>
        </div>
    </div>
  );
}
