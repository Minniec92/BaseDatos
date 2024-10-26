DELIMITER //
CREATE PROCEDURE ActualizarStatusProyectos()
BEGIN
    DECLARE ProyectoIdV INT;
    DECLARE FechaInicioV DATE;
    DECLARE FechaFinV DATE;
    DECLARE EstadoV VARCHAR(20);
    DECLARE done INT DEFAULT FALSE;

    DECLARE cursor_proyectos CURSOR FOR
    SELECT ProyectoId, FechaInicio, FechaFin, Estado FROM Proyectos;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cursor_proyectos;

    FETCH cursor_proyectos INTO ProyectoIdV, FechaInicioV, FechaFinV, EstadoV;

    WHILE NOT done DO
        BEGIN
 
            IF FechaFinV IS NOT NULL THEN
                IF CURDATE() > FechaFinV AND EstadoV <> 'Completado' THEN
                    UPDATE Proyectos SET Estado = 'Retrasado' WHERE ProyectoId = ProyectoIdV;
                ELSEIF CURDATE() <= FechaFinV AND EstadoV = 'Retrasado' THEN
                    UPDATE Proyectos SET Estado = 'En Curso' WHERE ProyectoId = ProyectoIdV;
                END IF;
            END IF;
            FETCH cursor_proyectos INTO ProyectoIdV, FechaInicioV, FechaFinV, EstadoV;
        END;
    END WHILE;

    CLOSE cursor_proyectos;

END//
DELIMITER ;
