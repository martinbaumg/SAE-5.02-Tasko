import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';

export const SidebarData = [
  {
    title: 'Home',
    path: '/',
    icon: <AiIcons.AiFillHome />,
    cName: 'nav-text',
  },
  {
    title: 'Test 1',
    path: '/test1',
    icon: <IoIcons.IoIosPaper />,
    cName: 'nav-text',
  },
  {
    title: 'Test 2',
    path: '/test2',
    icon: <IoIcons.IoIosFolder />,
    cName: 'nav-text',
  },
  {
    title: 'Test 3',
    path: '/test3',
    icon: <FaIcons.FaCartPlus />,
    cName: 'nav-text',
  },
  {
    title: 'Test 4',
    path: '/test4',
    icon: <AiIcons.AiFillAlert />,
    cName: 'nav-text',
  },
];
