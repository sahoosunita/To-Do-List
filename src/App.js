import "./App.css";

function App() {
  return (
    <div className="todo">
      <h1 className="todo_heading">To-Do List</h1>
      <div className="todo_body">
        <input type="text" placeholder="Add a task" className="todo_input" />
        <button className="add_button">Add</button>
      </div>
    </div>
  );
}

export default App;
