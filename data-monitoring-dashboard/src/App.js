import React, { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

function App() {
  const [metrics, setMetrics] = useState({
    integration_accuracy: 0,
    duplicate_rate: 0,
    missing_values: 0,
  });

  useEffect(() => {
    // Fetch fake data from Flask backend
    axios.get("http://127.0.0.1:5000/metrics")
      .then(response => setMetrics(response.data))
      .catch(error => console.error("Error fetching metrics:", error));
  }, []);

  // Data for Chart.js
  const data = {
    labels: ["Integration Accuracy", "Duplicate Rate", "Missing Values"],
    datasets: [
      {
        label: "Data Quality Metrics",
        data: [
          metrics.integration_accuracy,
          metrics.duplicate_rate,
          metrics.missing_values,
        ],
        backgroundColor: ["#4CAF50", "#FF9800", "#F44336"],
      },
    ],
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>Data Monitoring Dashboard</h2>
      <Bar data={data} />
      <br />
      <button
        style={{ padding: "10px", fontSize: "16px", cursor: "pointer" }}
        onClick={() => alert("File upload feature coming soon!")}
      >
        Upload Data File
      </button>
    </div>
  );
}

export default App;
