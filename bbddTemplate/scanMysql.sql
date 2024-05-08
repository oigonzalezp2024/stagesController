SELECT
conf.TABLE_SCHEMA,
conf.TABLE_NAME,
conf.ORDINAL_POSITION,
conf.COLUMN_NAME,
conf.DATA_TYPE,
REPLACE(REPLACE(REPLACE(conf.COLUMN_TYPE, conf.DATA_TYPE, ''), '(', ''), ')', '') AS 'DATA_LENGTH',
conf.COLUMN_KEY,
(
SELECT inncol.REF_COL_NAME
    FROM INNODB_SYS_FOREIGN_COLS AS inncol, 
    INNODB_SYS_FOREIGN as inn
    WHERE inncol.ID = inn.ID
    AND inn.FOR_NAME = CONCAT(CONCAT(conf.TABLE_SCHEMA,'/'),conf.TABLE_NAME)
    AND conf.COLUMN_KEY = 'MUL'
) as 'REF_COL_NAME',
(
    SELECT REPLACE(inn2.REF_NAME, CONCAT(conf.TABLE_SCHEMA,'/'), '')
    FROM INNODB_SYS_FOREIGN_COLS AS inncol2, 
    INNODB_SYS_FOREIGN as inn2
    WHERE inncol2.ID = inn2.ID
    AND inn2.FOR_NAME = CONCAT(CONCAT(conf.TABLE_SCHEMA,'/'),conf.TABLE_NAME)
    AND conf.COLUMN_KEY = 'MUL'
) as 'REF_NAME'
FROM
information_schema.COLUMNS as conf,
INNODB_SYS_FOREIGN_COLS AS inncol,
INNODB_SYS_FOREIGN as inn
WHERE conf.TABLE_SCHEMA != 'information_schema'
AND conf.TABLE_SCHEMA != 'mysql'
AND conf.TABLE_SCHEMA != 'performance_schema'
AND conf.TABLE_SCHEMA != 'phpmyadmin'
AND inncol.ID = inn.ID
ORDER by conf.TABLE_SCHEMA
AND conf.TABLE_NAME
AND conf.ORDINAL_POSITION;
