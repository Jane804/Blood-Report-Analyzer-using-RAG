import { useState } from "react";

import Upload from "./components/Upload";
import Chat from "./components/Chat";

import "./App.css";

function App() {

  const [summary, setSummary] =
    useState("");

  return (
    <div className="container">

      <h1>
        Blood Report Analyzer using RAG
      </h1>

      <Upload
        setSummary={setSummary}
      />

      <div className="card">

        <h2>Summary</h2>

        <div className="summary-box">
          {summary ||
            "Upload a report to generate summary"}
        </div>

      </div>

      <Chat />

    </div>
  );
}

export default App;