import { useState } from "react";
import API from "../api";

function Chat() {

  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const askQuestion = async () => {

    if (!question.trim()) {
      return;
    }

    try {

      setLoading(true);

      const response =
        await API.post("/chat", {
          question
        });

      setAnswer(
        response.data.answer
      );

    } catch (error) {

      console.error(error);

      alert("Error");

    } finally {

      setLoading(false);
    }
  };

  return (
    <div className="card">

      <h2>Ask Questions</h2>

      <input
        type="text"
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        placeholder="Ask about your blood report"
      />

      <button onClick={askQuestion}>
        {loading
          ? "Thinking..."
          : "Ask"}
      </button>

      <div className="answer-box">
        {answer}
      </div>

    </div>
  );
}

export default Chat;