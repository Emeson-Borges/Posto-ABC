import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AbastecimentosList from './components/AbastecimentosList/AbastecimentosList';
import RelatorioAbastecimentos from './components/RelatorioAbastecimentos';
import './styles/Menu.css';
import { CgHomeAlt } from "react-icons/cg";
import { CgPlayListCheck } from "react-icons/cg";

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">
              <CgHomeAlt /> Home
               </Link>
            </li>
            <li>
              <Link to="/abastecimentos">
              <CgPlayListCheck /> Lista de Abastecimentos
              </Link>
            </li>
            
          </ul>
        </nav>
        <Routes>
          <Route path="/abastecimentos" element={<AbastecimentosList />} />
          <Route path="/relatorio-abastecimentos" element={<RelatorioAbastecimentos />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
};

const Home = () => (
  <div>
    <h1>Bem-vindo ao Sistema de Gerenciamento!</h1>
  </div>
);

export default App;
