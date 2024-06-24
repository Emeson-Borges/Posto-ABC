import React, { useState } from 'react';
import axios from 'axios';
import { CgArrowDownO } from "react-icons/cg";
import { CgCommunity } from "react-icons/cg";

const RelatorioAbastecimentos = () => {
  const [pdfLink, setPdfLink] = useState(null);
  const [error, setError] = useState(null);

  const gerarRelatorio = async () => {
    try {
      const response = await axios.get('http://localhost:8000/relatorio-abastecimentos/', {
        responseType: 'arraybuffer', 
      });

      const blob = new Blob([response.data], { type: 'application/pdf' });
      const url = window.URL.createObjectURL(blob);
      setPdfLink(url);
      setError(null); 
    } catch (error) {
      console.error('Erro ao gerar o relatório:', error);
      setError('Não foi possível gerar o relatório. Por favor, tente novamente mais tarde.');
    }
  };

  return (
    <div>
      <h1>Relatório de Abastecimentos</h1>
      <button onClick={gerarRelatorio}> <CgCommunity /> Gerar Relatório PDF</button>
      {error && <p>{error}</p>}
      {pdfLink && (
        <div>
          <p>O relatório foi gerado com sucesso!</p>
          <a href={pdfLink} target="_blank" rel="noopener noreferrer" download="relatorio_abastecimentos.pdf">
            Baixar Relatório PDF <CgArrowDownO />
          </a>
        </div>
      )}
    </div>
  );
};

export default RelatorioAbastecimentos;
