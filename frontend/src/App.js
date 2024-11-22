import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Upload from './components/Upload';
import Display from './components/Display';
import Login from './components/Login';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/upload" component={Upload} />
          <Route path="/display" component={Display} />
          <Route path="/login" component={Login} />
          <Route path="/" exact component={Login} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
