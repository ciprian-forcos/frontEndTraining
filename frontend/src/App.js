import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomeScreen from './pages/HomeScreen';
import SecondScreen from './pages/SecondScreen';
import EditScreen from './pages/EditScreen';
import NoteScreen from './pages/NoteScreen';
import NavBar from './components/NavBar';


function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' Component={HomeScreen}/> 
        <Route path='/second' Component={SecondScreen}/>
        <Route path='/editScreen' Component={EditScreen}/>
        <Route path='/noteScreen/:pk' Component={NoteScreen}/>
      </Routes>
    </Router>
  );
}
  
export default App;
