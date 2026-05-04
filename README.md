# Journey-of-learning-python
In this repo I will learn all the fundamental concepts of python programming. I will cover all the topics chapter wise so it will be helpful for revision and also it will helpfull for others.

import { useEffect, useState } from "react";

export default function AuditPage() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/audit")
      .then((res) => res.json())
      .then((data) => setLogs(data));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Audit Logs</h1>

      <ul>
        {logs.map((log, i) => (
          <li key={i} className="border p-2 mb-2">
            {JSON.stringify(log)}
          </li>
        ))}
      </ul>
    </div>
  );
}
