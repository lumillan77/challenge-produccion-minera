

-- CONSULTAS

-- TOP 5 OPERADORES POR TONELADAS EXTRAIDAS

SELECT
    o.nombre_operador,
    SUM(rp.toneladas_extraidas) AS total_toneladas
FROM REGISTRO_PRODUCCION rp
JOIN OPERADOR o
    ON rp.operador_id = o.operador_id
GROUP BY o.nombre_operador
ORDER BY total_toneladas DESC
FETCH FIRST 5 ROWS ONLY;

-- PRODUCCION TOTAL X MES Y ZONA

SELECT
    TO_CHAR(fecha, 'YYYY-MM') AS mes,
    zona,
    SUM(toneladas_extraidas) AS total_toneladas
FROM REGISTRO_PRODUCCION
GROUP BY TO_CHAR(fecha, 'YYYY-MM'), zona
ORDER BY mes, zona;


-- EQUIPOS CON CONSUMO DE COMBUSTIBLE SOBRE EL PROMEDIO

SELECT
    equipo_id,
    AVG(consumo_combustible) AS consumo_promedio
FROM REGISTRO_PRODUCCION
GROUP BY equipo_id
HAVING AVG(consumo_combustible) >
       (SELECT AVG(consumo_combustible)
       FROM REGISTRO_PRODUCCION);
       
       
-- RELACION ENTRE HORAS OPERATIVAS E INCIDENTES

SELECT
    AVG(horas_operativas) AS promedio_horas,
    AVG(incidentes) AS promedio_incidentes
FROM REGISTRO_PRODUCCION;


-- RANKING DE ZONAS POR LEY DE MINERAL PROMEDIO

SELECT
    zona,
    AVG(ley_mineral) AS ley_promedio
FROM REGISTRO_PRODUCCION
GROUP BY zona
ORDER BY ley_promedio DESC;


-- EFICIENCIA PRODUCTIVA POR EQUIPO

SELECT
    equipo_id,
    ROUND(SUM(toneladas_extraidas) / SUM(horas_operativas), 2) AS toneladas_por_hora
FROM REGISTRO_PRODUCCION
GROUP BY equipo_id
ORDER BY toneladas_por_hora DESC;

-- OPERADORES CON MAYOR TASA DE INCIDENTES

SELECT
    o.nombre_operador,
    ROUND(SUM(rp.incidentes) / SUM(rp.horas_operativas), 3) AS incidentes_por_hora
FROM REGISTRO_PRODUCCION rp
JOIN OPERADOR o
    ON rp.operador_id = o.operador_id
GROUP BY o.nombre_operador
ORDER BY incidentes_por_hora DESC;





