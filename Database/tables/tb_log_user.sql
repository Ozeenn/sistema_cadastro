CREATE TABLE cadastro_pessoa.tb_log_user (
	oid_registro varchar(50) NULL,
	oid_usuario varchar(50) NULL,
	nom_user varchar(15) NULL,
	des_history varchar NULL,
	dat_event date NULL,
	CONSTRAINT uc_oid_registro_log UNIQUE (oid_registro)
);