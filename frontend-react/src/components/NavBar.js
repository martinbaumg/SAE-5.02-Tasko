import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';
import './NavBar.css';
import { IconContext } from 'react-icons';
import {
  FaBars,
  FaTimes,
  FaSearch,
  FaPlus,
  FaFolder,
  FaFolderOpen,
  FaList,
} from 'react-icons/fa';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

function NavBar() {
  const [sidebar, setSidebar] = useState(false);
  const [directories, setDirectories] = useState([
    {
      id: 1,
      name: 'Directory 1',
      tasks: [
        {
          id: 1,
          name: 'Task 1',
          description: 'Description of Task 1',
        },
        {
          id: 2,
          name: 'Task 2',
          description: 'Description of Task 2',
        },
      ],
      isOpen: false,
    },
  ]);
  const [lists, setLists] = useState([
    {
      id: 1,
      name: 'List 1',
      tasks: [
        {
          id: 5,
          name: 'Task 5',
          description: 'Description of Task 5',
        },
        {
          id: 6,
          name: 'Task 6',
          description: 'Description of Task 6',
        },
      ],
    },
  ]);
  const [showAddListModal, setShowAddListModal] = useState(false);
  const [showAddDirectoryModal, setShowAddDirectoryModal] = useState(false);
  const [newListName, setNewListName] = useState('');
  const [newDirectoryName, setNewDirectoryName] = useState('');
  const [showAddListButton, setShowAddListButton] = useState(true);
  const [showAddDirectoryButton, setShowAddDirectoryButton] = useState(true);

  const showSidebar = () => setSidebar(!sidebar);

  const addList = (directoryId) => {
    setShowAddListModal({ show: true, directoryId });
  };

  const addDirectory = () => {
    setShowAddDirectoryModal(true);
  };

  const toggleDirectory = (id) => {
    const updatedDirectories = directories.map((directory) => {
      if (directory.id === id) {
        return { ...directory, isOpen: !directory.isOpen };
      } else {
        return directory;
      }
    });
    setDirectories(updatedDirectories);
  };

  const handleLinkClick = (event) => {
    event.stopPropagation();
  };

  const handleDirectoryClick = (event, id) => {
    event.stopPropagation();
    toggleDirectory(id);
  };

  const handleAddListSubmit = (event) => {
    event.preventDefault();
    const newList = {
      id: lists.length + 1,
      name: newListName,
      tasks: [],
    };
    if (showAddListModal.directoryId) {
      const updatedDirectories = directories.map((directory) => {
        if (directory.id === showAddListModal.directoryId) {
          return { ...directory, tasks: [...directory.tasks, newList] };
        } else {
          return directory;
        }
      });
      setDirectories(updatedDirectories);
    } else {
      setLists([...lists, newList]);
    }
    setShowAddListModal(false);
    setNewListName('');
  };

  const handleAddDirectorySubmit = (event) => {
    event.preventDefault();
    const newDirectory = {
      id: directories.length + 1,
      name: newDirectoryName,
      tasks: [],
      isOpen: false,
    };
    setDirectories([...directories, newDirectory]);
    setShowAddDirectoryModal(false);
    setNewDirectoryName('');
  };

  const handleDragStart = () => {
    setShowAddListButton(false);
    setShowAddDirectoryButton(false);
  };

  const handleDragEnd = (result) => {
    if (!result.destination) {
      return;
    }

    if (result.type === 'list') {
      const updatedLists = Array.from(lists);
      const [removed] = updatedLists.splice(result.source.index, 1);
      updatedLists.splice(result.destination.index, 0, removed);

      setLists(updatedLists);
    } else if (result.type === 'directory') {
      const updatedDirectories = Array.from(directories);
      const [removed] = updatedDirectories.splice(result.source.index, 1);
      updatedDirectories.splice(result.destination.index, 0, removed);

      setDirectories(updatedDirectories);
    }

    setShowAddListButton(true);
    setShowAddDirectoryButton(true);
  };

  return (
    <>
      <IconContext.Provider value={{ color: '#fff' }}>
        <div className="navbar">
          <Link to="#" className="menu-bars-open">
            <FaBars onClick={showSidebar} />
          </Link>
          <div className="navbar-logo">
            <Link to="/">Logo</Link>
          </div>
          <div className="search-bar">
            <input type="text" placeholder="Search..." />
            <button>
              <FaSearch />
            </button>
          </div>
        </div>
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
          <DragDropContext
            onDragStart={handleDragStart}
            onDragEnd={handleDragEnd}
          >
            <Droppable droppableId="lists">
              {(provided) => (
                <ul
                  className="nav-menu-items"
                  {...provided.droppableProps}
                  ref={provided.innerRef}
                >
                  {showAddListButton && (
                    <li className="nav-text">
                      <div className="nav-link" onClick={() => addList()}>
                        <FaPlus />
                        <span>Add List</span>
                      </div>
                    </li>
                  )}
                  {lists.map((list, index) => {
                    return (
                      <Draggable
                        key={list.id}
                        draggableId={list.id.toString()}
                        index={index}
                        type="list"
                      >
                        {(provided) => (
                          <li
                            className="nav-text"
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                          >
                            <div className="nav-link">
                              <FaList />
                              <Link to="#" onClick={handleLinkClick}>
                                {list.name}
                              </Link>
                            </div>
                          </li>
                        )}
                      </Draggable>
                    );
                  })}
                  {showAddDirectoryButton && (
                    <li className="nav-text">
                      <div className="nav-link" onClick={() => addDirectory()}>
                        <FaPlus />
                        <span>Add Directory</span>
                      </div>
                    </li>
                  )}
                  {directories.map((directory, index) => {
                    return (
                      <Draggable
                        key={directory.id}
                        draggableId={directory.id.toString()}
                        index={index}
                        type="directory"
                      >
                        {(provided) => (
                          <li
                            key={directory.id}
                            className="nav-text"
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                          >
                            <div
                              className="nav-link"
                              onClick={(event) =>
                                handleDirectoryClick(event, directory.id)
                              }
                            >
                              {directory.isOpen ? (
                                <FaFolderOpen />
                              ) : (
                                <FaFolder />
                              )}
                              <span>{directory.name}</span>
                            </div>
                            {directory.isOpen &&
                              directory.tasks.map((task) => {
                                return (
                                  <ul key={task.id} className="nav-submenu">
                                    <li className="nav-text">
                                      <div className="nav-link">
                                        <FaList />
                                        <Link to="#" onClick={handleLinkClick}>
                                          {task.name}
                                        </Link>
                                      </div>
                                    </li>
                                  </ul>
                                );
                              })}
                          </li>
                        )}
                      </Draggable>
                    );
                  })}
                  {provided.placeholder}
                </ul>
              )}
            </Droppable>
          </DragDropContext>
        </nav>
        {showAddListModal.show && (
          <div className="modal-overlay">
            <div className="modal">
              <div className="modal-content">
                <h2>Add List</h2>
                <form onSubmit={handleAddListSubmit}>
                  <label htmlFor="newListName">List Name:</label>
                  <input
                    type="text"
                    id="newListName"
                    value={newListName}
                    onChange={(event) => setNewListName(event.target.value)}
                  />
                  <button type="submit">Add List</button>
                  <button onClick={() => setShowAddListModal(false)}>
                    Cancel
                  </button>
                </form>
              </div>
            </div>
          </div>
        )}
        {showAddDirectoryModal && (
          <div className="modal-overlay">
            <div className="modal">
              <div className="modal-content">
                <h2>Add Directory</h2>
                <form onSubmit={handleAddDirectorySubmit}>
                  <label htmlFor="newDirectoryName">Directory Name:</label>
                  <input
                    type="text"
                    id="newDirectoryName"
                    value={newDirectoryName}
                    onChange={(event) =>
                      setNewDirectoryName(event.target.value)
                    }
                  />
                  <button type="submit">Add Directory</button>
                  <button onClick={() => setShowAddDirectoryModal(false)}>
                    Cancel
                  </button>
                </form>
              </div>
            </div>
          </div>
        )}
      </IconContext.Provider>
    </>
  );
}

export default NavBar;
