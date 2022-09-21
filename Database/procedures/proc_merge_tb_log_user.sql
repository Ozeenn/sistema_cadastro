CREATE OR REPLACE PROCEDURE staging.proc_merge_tb_log_user()
 LANGUAGE plpgsql
AS $procedure$
	begin
--		truncate table etl_api.tb_profile_infos;
		insert into cadastro_pessoa.tb_log_user 
			select  
			md5(lu.nom_user || lu.dat_event::varchar) as oid_registro,
							tc.oid_user as oid_usuario,
							lu.nom_user,
							lu.des_history,
							lu.dat_event
			from staging.stg_log_user lu 
			inner JOIN cadastro_pessoa.tb_cadastro tc on lu.nom_user=tc.nom_user
			ON CONFLICT ( oid_registro  ) DO UPDATE set des_history  = EXCLUDED.des_history
			;

	END;
$procedure$
;