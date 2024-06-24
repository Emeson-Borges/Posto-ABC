import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate, Link} from 'react-router-dom';
import '../AbastecimentosList/AbastecimentosList.css';
import { FiCalendar } from "react-icons/fi";
import { LiaMoneyBillWaveSolid } from "react-icons/lia";
import { LuFileText } from "react-icons/lu";
import { FiCornerDownLeft } from "react-icons/fi";
import { CgAddR } from "react-icons/cg";
import { CgArrowTopRight } from "react-icons/cg";
import { CgServer } from "react-icons/cg";
import { BsBarChart } from "react-icons/bs";



const AbastecimentosList = () => {
  const [abastecimentos, setAbastecimentos] = useState([]);
  const [bombas, setBombas] = useState([]);
  const [tanques, setTanques] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    bomba: '',
    tanque: '',
    data: '',
    quantidade_litros: '',
    valor_abastecido: '',
  });
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [abastecimentosResponse, bombasResponse, tanquesResponse] = await Promise.all([
          axios.get('http://localhost:8000/api/abastecimentos/'),
          axios.get('http://localhost:8000/api/bombas/'),
          axios.get('http://localhost:8000/api/tanques/'),
        ]);
        setAbastecimentos(abastecimentosResponse.data);
        setBombas(bombasResponse.data);
        setTanques(tanquesResponse.data);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const valorAbastecido = parseFloat(formData.valor_abastecido);
      const imposto = (valorAbastecido * 0.13).toFixed(2);

      const response = await axios.post('http://localhost:8000/api/abastecimentos/', {
        bomba: formData.bomba,
        data: formData.data,
        quantidade_litros: parseFloat(formData.quantidade_litros),
        valor_abastecido: valorAbastecido,
        imposto: imposto,
      });

      setAbastecimentos([...abastecimentos, response.data]);
      setFormData({
        bomba: '',
        tanque: '',
        data: '',
        quantidade_litros: '',
        valor_abastecido: '',
      });
    } catch (error) {
      console.error('Erro ao criar abastecimento:', error.response?.data || error.message);
    }
  };

  if (loading) {
    return <div className="loading">Carregando...</div>;
  }

  return (
    <div className="container">
      <h1>Lista de Abastecimentos</h1>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="tanque">Tanque</label>
          <select
            id="tanque"
            name="tanque"
            value={formData.tanque}
            onChange={handleChange}
            required
          >
            <option value="">Selecione o tanque</option>
            {tanques.map((tanque) => (
              <option key={tanque.id} value={tanque.id}>
                {tanque.tipo_combustivel}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="bomba">Bomba</label>
          <select
            id="bomba"
            name="bomba"
            value={formData.bomba}
            onChange={handleChange}
            required
          >
            <option value="">Selecione a bomba</option>
            {bombas.map((bomba) => (
              <option key={bomba.id} value={bomba.id}>
                {bomba.bomba_utilizada}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="data">Data</label>
          <input
            type="date"
            id="data"
            name="data"
            value={formData.data}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="quantidade_litros">Quantidade de Litros</label>
          <input
            type="number"
            id="quantidade_litros"
            name="quantidade_litros"
            value={formData.quantidade_litros}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="valor_abastecido">Valor Abastecido</label>
          <input
            type="number"
            id="valor_abastecido"
            name="valor_abastecido"
            value={formData.valor_abastecido}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit"> <CgAddR /> Adicionar Abastecimento</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>Data <FiCalendar /></th>
            <th>Tanque <CgServer /></th>
            <th>Bomba <CgServer /></th>
            <th>Valor Abastecido <LiaMoneyBillWaveSolid /></th>
            <th>Imposto (13%) <CgArrowTopRight /></th>
            <th>Valor por Litro <BsBarChart /></th>
          </tr>
        </thead>
        <tbody>
        {abastecimentos.map((abastecimento) => (
          <tr key={abastecimento.id}>
            <td>{abastecimento.data}</td>
            <td>{abastecimento.bomba?.tanque?.tipo_combustivel}</td>
            <td>{abastecimento.bomba}</td>
            <td>R$ {parseFloat(abastecimento.valor_abastecido).toFixed(2)}</td>
            <td>R$ {parseFloat(abastecimento.imposto).toFixed(2)}</td>
            <td>R$ {(abastecimento.valor_abastecido / abastecimento.quantidade_litros).toFixed(2)}</td>
          </tr>
        ))}
        </tbody>
      </table>

      <div className="buttons-container">
        <button onClick={() => navigate(-1)}><FiCornerDownLeft /> Voltar</button>
        <Link to="/relatorio-abastecimentos" className="button-link"> <LuFileText /> Gerar Relatório</Link>
      </div>
    </div>
  );
};

export default AbastecimentosList;
