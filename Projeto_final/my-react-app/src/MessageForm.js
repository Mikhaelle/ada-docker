import React, { useState } from "react";
import axios from "axios";

const MessageForm = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false); // Add loading state

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true); // Set loading state to true
    try {
      const res = await axios.post("http://localhost:5000/insert", {
        message: message,
      });
      console.log(res);
      setResponse(`Mensagem ${message} guardada no banco com successo`);
    } catch (error) {
      console.error("Error:", error);
      setResponse("Error inserting message.");
    } finally {
      setIsLoading(false); // Reset loading state after request completes
    }
  };

  return (
    <div>
      <h2>Insert Message</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Message:
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </label>
        <button type="submit" disabled={isLoading}>
          Submit
        </button>
        {isLoading && <span>Loading...</span>} {/* Show loading indicator */}
      </form>
      {response && <p>{response}</p>}
    </div>
  );
};

export default MessageForm;
