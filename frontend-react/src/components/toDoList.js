import React, { useState } from 'react'; 
import './toDoList.css';

const ToDoList = () => {
    const [todos, setTodos] = useState ([]);
    const [newTodo, setNewTodo] = useState("");

    const handelAddTodo = () => {
        if (newTodo.trim() !== "") {
            setTodos([...todos, {text: newTodo.trim(), checked: false }]);
            setNewTodo("");
        }
    }
    
    const handelDeleteTodo = (index) => {
        const newTodos = [...todos];
        newTodos.splice(index, 1);
        setTodos(newTodos);
    };

    const handelToggleTodo = (index) => {
       const newTodos = [...todos];
       newTodos[index].checked = !newTodos[index].checked;
       setTodos(newTodos);
    };

    return ( 
        <div>
            <input className="input" type="text" value={newTodo} onChange={(e) => setNewTodo(e.target.value)}/>
            <button className="addButton" onClick={handelAddTodo}>Add</button>
            <ul>
                {todos.map((todo, index) => (
                    <li className="checkli" key={index}>
                    <div className="checklist">

                    <input type="checkbox" checked={todo.checked} onChange={() => handelToggleTodo(index)}/>
                    <span className="tasks" style={{ textDecoration: todo.checked ? "line-through" : "none" }} >{todo.text}</span>
                    <button classname="deleteButton" onClick={() => handelDeleteTodo(index)}>
                         Delete
                    </button>   
                    </div>
                   </li>
                ))}
            </ul>
        </div>
    );
};

export default ToDoList; 
