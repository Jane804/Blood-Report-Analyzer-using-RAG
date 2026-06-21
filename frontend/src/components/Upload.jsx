import { useState } from "react";
import API from "../api";

function Upload({ setSummary }) {

  const [file, setFile] = useState(null);
  const [loading, setLoading] =
    useState(false);

  const uploadFile = async () => {

    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      setLoading(true);

      await API.post(
        "/upload",
        formData
      );

      const summaryResponse =
        await API.get("/summary");

      setSummary(
        summaryResponse.data.summary
      );

      alert("Upload Successful");

    } catch (error) {

      console.error(error);

      alert("Upload Failed");

    } finally {

      setLoading(false);
    }
  };

  return (
    <div className="card">

      <h2>Upload Blood Report</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <br />

      <button onClick={uploadFile}>
        {loading
          ? "Uploading..."
          : "Upload"}
      </button>

    </div>
  );
}

export default Upload;