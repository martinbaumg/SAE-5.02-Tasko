import React, { useState } from 'react';
import './toDoList.css';
import { faTrash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const ToDoList = ({ onAddTodo }) => {
  const [todos, setTodos] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [newTodo, setNewTodo] = useState('');

  const handleAddTodo = () => {
    if (newTodo.trim() !== '') {
      setTodos([...todos, { text: newTodo.trim(), checked: false }]);
      setNewTodo('');
      setShowModal(false);
      onAddTodo(newTodo.trim());
    }
  };

  const handleDeleteTodo = (index) => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  const handleToggleTodo = (index) => {
    const newTodos = [...todos];
    newTodos[index].checked = !newTodos[index].checked;
    setTodos(newTodos);
  };

  return (
    <div className="to-do-list">
      <h1 className="to-do-list__title">To-Do List</h1>
      <button className="to-do-list__button" onClick={() => setShowModal(true)}>
        Add Task
      </button>
      <ul className="to-do-list__checklist">
        {todos.map((todo, index) => (
          <li className="to-do-list__checklist-item" key={index}>
            <input
              className="to-do-list__checklist-item-checkbox"
              type="checkbox"
              checked={todo.checked}
              onChange={() => handleToggleTodo(index)}
            />
            <span
              className={`to-do-list__checklist-item-text ${
                todo.checked ? 'to-do-list__checklist-item-text--completed' : ''
              }`}
            >
              {todo.text}
            </span>
            <button
              className="to-do-list__button to-do-list__button--delete"
              onClick={() => handleDeleteTodo(index)}
            >
              <FontAwesomeIcon icon={faTrash} />
            </button>
          </li>
        ))}
      </ul>
      <div className={`to-do-list__modal-overlay ${showModal ? 'show' : ''}`}>
        <div className={`to-do-list__modal ${showModal ? 'show' : ''}`}>
          <div className="to-do-list__modal-content">
            <h2 className="to-do-list__modal-title">Add a New Task</h2>
            <input
              className="to-do-list__modal-input"
              type="text"
              placeholder="Enter task description"
              value={newTodo}
              onChange={(e) => setNewTodo(e.target.value)}
            />
            <div className="to-do-list__modal-buttons">
              <button
                className="to-do-list__button"
                onClick={() => setShowModal(false)}
              >
                Cancel
              </button>
              <button className="to-do-list__button" onClick={handleAddTodo}>
                Add
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ToDoList;
