CREATE OR REPLACE PROCEDURE staging.proc_insert_tb_cadastro()
 LANGUAGE plpgsql
AS $procedure$
	begin
		insert into cadastro_pessoa.tb_cadastro  
			select  
				md5(nom_user) as oid_user,
				nom_user as nom_user,
				des_password, 
				dat_cadastro 
			from staging.stg_cadastro stg
			where not exists (
				select 1 from cadastro_pessoa.tb_cadastro tb
				where md5(stg.nom_user) = tb.oid_user
			)
		
			;

	END;
$procedure$
;