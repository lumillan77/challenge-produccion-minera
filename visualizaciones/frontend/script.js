

// ===============================
// CONFIGURACIÓN
// ===============================
const API_URL = "http://localhost:8000/produccion?limit=200";

let datosOriginales = [];

// ===============================
// CARGA INICIAL
// ===============================
fetch(API_URL)
  .then(response => response.json())
  .then(data => {
    datosOriginales = data;
    cargarFiltros(data);
    actualizarDashboard(data);
    renderTabla(data);
  })
  .catch(error => {
    console.error("Error al consumir la API:", error);
  });

// ===============================
// DASHBOARD
// ===============================
function actualizarDashboard(datos) {
  const totalToneladas = datos.reduce(
    (suma, item) => suma + (item.toneladas_extraidas || 0),
    0
  );

  document.getElementById("totalToneladas").textContent =
    totalToneladas.toFixed(2);

  document.getElementById("totalRegistros").textContent = datos.length;
}

// ===============================
// TABLA
// ===============================
function renderTabla(datos) {
  const tbody = document.getElementById("tablaDatos");
  tbody.innerHTML = "";

  datos.forEach(item => {
    const fila = document.createElement("tr");

    fila.innerHTML = `
      <td>${item.fecha}</td>
      <td>${item.turno}</td>
      <td>${item.equipo_id}</td>
      <td>${item.operador}</td>
      <td>${item.zona}</td>
      <td>${item.toneladas_extraidas}</td>
    `;

    tbody.appendChild(fila);
  });
}

// ===============================
// FILTROS
// ===============================
function cargarFiltros(datos) {
  cargarSelect("filtroZona", datos.map(d => d.zona));
  cargarSelect("filtroEquipo", datos.map(d => d.equipo_id));
  cargarSelect("filtroOperador", datos.map(d => d.operador));
}

function cargarSelect(id, valores) {
  const select = document.getElementById(id);

  [...new Set(valores)].forEach(valor => {
    if (valor) {
      const option = document.createElement("option");
      option.value = valor;
      option.textContent = valor;
      select.appendChild(option);
    }
  });
}

// ===============================
// APLICAR FILTROS
// ===============================
document.getElementById("filtroZona").addEventListener("change", aplicarFiltros);
document.getElementById("filtroEquipo").addEventListener("change", aplicarFiltros);
document.getElementById("filtroOperador").addEventListener("change", aplicarFiltros);

function aplicarFiltros() {
  const zona = document.getElementById("filtroZona").value;
  const equipo = document.getElementById("filtroEquipo").value;
  const operador = document.getElementById("filtroOperador").value;

  const filtrados = datosOriginales.filter(item =>
    (!zona || item.zona === zona) &&
    (!equipo || item.equipo_id === equipo) &&
    (!operador || item.operador === operador)
  );

  actualizarDashboard(filtrados);
  renderTabla(filtrados);
}


// ===============================
// RANKING DE OPERADORES
// ===============================

//Consumir el ranking desde la API

fetch("http://localhost:8000/ranking/operadores")
  .then(response => response.json())
  .then(data => {
    renderRanking(data);
    renderGrafico(data);
  });

  //Mostrar el ranking en tabla

  function renderRanking(data) {
  const tbody = document.getElementById("tablaRanking");
  tbody.innerHTML = "";

  data.forEach(item => {
    const fila = `
      <tr>
        <td>${item.operador}</td>
        <td>${item.toneladas_extraidas.toFixed(2)}</td>
      </tr>
    `;
    tbody.innerHTML += fila;
  });
}

//Crear el gráfico (Chart.js

function renderGrafico(data) {
  const labels = data.map(item => item.operador);
  const valores = data.map(item => item.toneladas_extraidas);

  const ctx = document.getElementById("graficoOperadores").getContext("2d");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Producción Promedio",
        data: valores
      }]
    }
  });
}