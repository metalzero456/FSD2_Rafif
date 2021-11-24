
import logo from './logo.svg';
import './App.css';
import PersonInformation from './components/PersonInformation'
import FetchComponent from './components/FetchComponent';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <PersonInformation />
        <FetchComponent />
      </header>
    </div>
  );
}

export default App;
