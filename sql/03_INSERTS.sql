
-- INSERTS

-- TABLA OPERADOR

INSERT INTO OPERADOR (nombre_operador)
SELECT DISTINCT operador
FROM PRODUCCION_MINERA;

SELECT * FROM OPERADOR;

-- TABLA EQUIPO 

INSERT INTO EQUIPO (equipo_id)
SELECT DISTINCT equipo_id
FROM PRODUCCION_MINERA;

SELECT * FROM EQUIPO;

-- REGISTROS DE PRODUCCION

INSERT INTO REGISTRO_PRODUCCION (
    fecha,
    turno,
    zona,
    toneladas_extraidas,
    horas_operativas,
    consumo_combustible,
    incidentes,
    ley_mineral,
    operador_id,
    equipo_id
)
SELECT
    pm.fecha,
    pm.turno,
    pm.zona,
    pm.toneladas_extraidas,
    pm.horas_operativas,
    pm.consumo_combustible,
    pm.incidentes,
    pm.ley_mineral,
    o.operador_id,
    pm.equipo_id
FROM PRODUCCION_MINERA pm
JOIN OPERADOR o
    ON pm.operador = o.nombre_operador;
    
SELECT COUNT(*) FROM REGISTRO_PRODUCCION;


-- PRUEBA

SELECT rp.fecha, o.nombre_operador, rp.equipo_id, rp.toneladas_extraidas
FROM REGISTRO_PRODUCCION rp
JOIN OPERADOR o ON rp.operador_id = o.operador_id
FETCH FIRST 5 ROWS ONLY;


