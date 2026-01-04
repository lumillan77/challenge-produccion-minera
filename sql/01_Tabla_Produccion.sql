
CREATE TABLE produccion_minera (
    fecha DATE,
    turno VARCHAR2(10),
    equipo_id VARCHAR2(10),
    operador VARCHAR2(50),
    zona VARCHAR2(20),
    toneladas_extraidas NUMBER(10,2),
    horas_operativas NUMBER(10,2),
    consumo_combustible NUMBER(10,2),
    incidentes NUMBER,
    ley_mineral NUMBER(5,2)
);

SELECT * FROM produccion_minera;
SELECT COUNT(*) FROM produccion_minera;
SELECT * FROM produccion_minera FETCH FIRST 5 ROWS ONLY;



