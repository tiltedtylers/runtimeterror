import React, { useEffect, useState } from "react";
import axios from "axios";

const CheckDBConnection = () => {
  const [dbconnection, setDbconnection] = useState(false);
  useEffect(() => {
    async function checkDbConnection() {
      axios.get("http://localhost:8090/dbconnect").then((res) => {
        if (res.data.toString() === "true") {
          setDbconnection(true);
        } else {
          setDbconnection(false);
        }
      });
    }
    checkDbConnection();
  }, []);
  return (
    <div>
      {dbconnection
        ? "Database connection is successful"
        : "Database connection is loading..."}
    </div>
  );
};

export default CheckDBConnection;
