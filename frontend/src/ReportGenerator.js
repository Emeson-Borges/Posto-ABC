// src/ReportGenerator.js

import React, { useState } from 'react';
import axios from 'axios';
import { saveAs } from 'file-saver';

const ReportGenerator = () => {
  const [loading, setLoading] = useState(false);

  const handleGenerateReport = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/relatorio-abastecimentos/', {
        responseType: 'blob',  // Importante para receber um blob (arquivo) como resposta
      });
      
      // Salva o arquivo de PDF
      const pdfBlob = new Blob([response.data], { type: 'application/pdf' });
      saveAs(pdfBlob, 'relatorio_abastecimentos.pdf');
    } catch (error) {
      console.error('Erro ao gerar relatório:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Gerador de Relatórios</h2>
      <button onClick={handleGenerateReport} disabled={loading}>
        {loading ? 'Gerando Relatório...' : 'Gerar Relatório em PDF'}
      </button>
    </div>
  );
};

export default ReportGenerator;
