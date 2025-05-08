import React from "react";
import { Link } from "react-router-dom";

function AdminDashboard() {
  return (
    <div>
      <h2>Admin Dashboard</h2>
      <Link to="/optimize">Optimize Routes</Link>
      <br />
      <Link to="/users">View Users</Link>
    </div>
  );
}

export default AdminDashboard;
