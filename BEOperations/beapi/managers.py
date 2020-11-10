from django.db import models, connection


class JobManager(models.Manager):
    def jobs_view_procedure(self, username, section,status):
        with connection.cursor() as cursor:
            cursor.callproc(
                'core.jobs_view_fx', [username,section,status])
            result = cursor.fetchall()
            result_list = []
            for row in result:
                results = {
                    "job_id": row[0],
                    "work_order_id": row[1],
                    "created_by":row[2],
                    "created_on":row[3],
                    "modified_by":row[4],
                    "modified_on":row[5],
                    "type":row[6],
                    "description":row[7],
                    "asset_id":row[8],
                    "assignee":row[9],
                    "comments":row[10],
                    "closed_by":row[11],
                    "closed_dt":row[12],
                    "asset_name":row[13],
                    "asset_type":row[14],
                    "asset_number":row[15],
                    "expected_end_dt":row[16],
                    "reference_no":row[17],
                    "asset_serial":row[18],
                    "status":row[19],
                    "trigger":row[20],
                    "start_date":row[21],
                    "status_value":row[22],
                }
                result_list.append(results)
            return result_list

    def job_workflow_status(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("""
                        SELECT roleprofile.profile_code ,workflow.section,userprofile.username as responsible ,jobworkflow.ec_num,jobworkflow.action
                        FROM core.job
                        INNER JOIN core.workflow on workflow.workflow_code = job.workflow_id
                        INNER JOIN core.roleprofile on roleprofile.role_code =  workflow.role_code
                        INNER JOIN core.userprofile on userprofile.profile_code = roleprofile.profile_code and userprofile.status='Active'
                        LEFT JOIN core.jobworkflow on workflow.workflow_id = jobworkflow.workflow_id
                        WHERE job.job_id = %s  ORDER BY workflow.step""", params=[pk]
                           )
            result_list = []
            for row in cursor.fetchall():
                results = {
                    "profile_code": row[0],
                    "section": row[1],
                    "responsible": row[2],
                    "ec_num": row[3],
                    "action": row[4]
                }
                result_list.append(results)
        return result_list


class JobWorkflowManager(models.Manager):
    def job_awaiting_action_procedure(self, ec_num):
        with connection.cursor() as cursor:
            cursor.callproc(
                'core.jobs_awaiting_action_fx', [ec_num, ])
            result = cursor.fetchall()
            result_list = []
            for row in result:
                results = {
                   "job_id": row[0],
                    "created_by":row[1],
                    "created_on":row[2],
                    "work_order_id": row[3],
                    "type":row[4],
                    "description":row[5],
                    "assignee":row[6],
                    "comments":row[7],
                    "closed_by":row[8],
                    "closed_dt":row[9],
                    "status":row[10],
                    "approve":row[11],
                    "reject":row[12],
                    "role_name":row[13],
                    "status_value":row[14],
                    "job_form":row
                }
                result_list.append(results)
        return result_list

    def job_workflow_procedure(self, job_id):
        with connection.cursor() as cursor:
            cursor.callproc(
                'core.job_workflow_fx', [job_id, ])
            result = cursor.fetchall()
            result_list = []
            for row in result:
                results = {
                    "profile_code": row[0],
                    "section": row[1],
                    "responsible": row[2],
                    "ec_num": row[3],
                    "action": row[4],
                    "created_on": row[5],
                    "action_dt": row[6],
                    "step": row[7],
                    "comments": row[8]
                }
                result_list.append(results)
            return result_list

        def approve_job(self,job_workflow_id,job_id,actioner,decision):
            with connection.cursor() as cursor:
                return cursor.callproc(
                    'core.approve_job',[job_workflow_id,job_id,actioner,decision])      
            


class AssetRelationshipManager(models.Manager):
    def station_assets(self, parent_assetid):
        with connection.cursor() as cursor:

            cursor.callproc(
            'core.stationtransformers_fx', [parent_assetid])
            transformers = cursor.fetchall()

            cursor.callproc(
            'core.stationfeeders_fx', [parent_assetid])
            feeders = cursor.fetchall()

            cursor.callproc(
            'core.stationswitchgears_breakers_fx', [parent_assetid])
            breakers = cursor.fetchall()

            cursor.callproc(
            'core.stationswitchgear_isolators_fx', [parent_assetid])
            isolators = cursor.fetchall()


            result_list = []
            assets={}
            transformer_list=[]
            for row in transformers:
                result = {
                    "transformerid": row[0],
                    "name": row[1],
                    "voltageratio": row[2],
                    "sscode": row[3],
                    "depot" :row[4] ,
                    "district":row[5], 
                    "region": row[6],
                    "assetno":row[7],
                    "createdon": row[8],
                    "createdby": row[9],
                    "modifiedon": row[10],
                    "modifiedby": row[11],
                    "comments": row[12],
                    "status": row[13],
                    "districtid": row[14],
                    "wardid": row[15],
                    "provinceid": row[16],
                    "id": row[17],
                    "serialno": row[18],
                    "systemno": row[19],
                    "highvoltage":row[20],
                    "lowvoltage":row[21],
                    "application": row[22],
                    "mounting": row[23],
                    "standard": row[24],
                    "make": row[25],
                    "transformerinsulation": row[26],
                    "manufactureryear":row[27],
                    "installationyear": row[28],
                    "commissionyear": row[29],
                    "windingsno": row[30],
                    "bil": row[31],
                    "mass": row[32],
                    "vectorgroup": row[33],
                    "impedance":row[34],
                    "ironlosses": row[35],
                    "copperlosses": row[36],
                    "taperange": row[37],
                    "cooling": row[38],
                    "capacity": row[39],
                    "geom2d": row[40],
                    "maxcapacity": row[41],
                    "windings": row[42],
                    "geom3d": row[43],
                    "asset_change": row[44],
                    "trregion": row[45],
                }
                transformer_list.append(result) 
            assets['transformers']=transformer_list

            feeder_list=[]
            for row in feeders:
                result = {
                    "feedercode": row[0],
                    "name": row[1],
                    "voltagelevel": row[2] ,
                    "depot":row[3],
                    "district": row[4],
                    "region":row[5],
                    "assetno":row[6],
                    "createdon": row[7],
                    "createdby": row[8],
                    "modifiedon":row[9],
                    "feederno":row[10],
                    "modifiedby":row[11],
                    "comments":row[12],
                    "status":row[13],
                    "districtid":row[14],
                    "wardid":row[15],
                    "provinceid":row[16],
                    "id":row[17],
                    "geom2d": row[18],
                    "sourcesscode":row[19],
                    "asset_change":row[20],
                    "trregion":row[21]                                    
                }
                feeder_list.append(result)
            assets['feeders'] = feeder_list
    
            breaker_list=[]
            for row in breakers:
                result = {
                    "switchgearno": row[0],
                    "switchgearid": row[1],
                    "type": row[2] ,
                    "voltagerating":row[3],
                    "make":row[4],
                    "depot": row[5],
                    "district":row[6],
                    "region":row[7],
                    "assetno":row[8],
                    "createdon": row[9],
                    "createdby": row[10],
                    "modifiedon": row[11],
                    "modifiedby":row[12],
                    "comments":row[13],
                    "status":row[14],
                    "districtid":row[15],
                    "wardid":row[16],
                    "provinceid":row[17],
                    "id":row[18],
                    "serialno":row[19],
                    "model":row[20],
                    "constructiontype": row[21],
                    "mco":row[22],
                    "opmech": row[23],
                    "busbarsno":row[24],
                    "optype": row[25],
                    "standard":row[26],
                    "insulationmedium": row[27],
                    "interruptingmedium":row[28],
                    "ratedcc":row[29],
                    "ratedscbc":row[30],
                    "ratedmc":row[31],
                    "ratedscwt":row[32],
                    "ratedstwc":row[33],
                    "controlvoltage":row[34],
                    "motorost":row[35],
                    "motorvoltage":row[36],
                    "auxvoltage":row[37],
                    "possiblecountsetting":row[38],
                    "autoreclosingtype":row[39],
                    "dutycycle":row[40],
                    "netmass":row[41],
                    "ocinstalled":row[42],
                    "bil":row[43],
                    "commissionyear":row[44],
                    "installationyear":row[45],
                    "baytype": row[46],
                    "use":row[47],
                    "tripcoilsno":row[48],
                    "normalopstatus": row[49],
                    "cdpoint":row[50],
                    "feedercode":row[51],
                    "geom2d": row[52],
                    "mvboard":row[53],
                    "geom3d":row[54],
                    "nostatus":row[55],
                    "manufactureyear":row[56],
                    "installed_on":row[57],
                    "asset_change":row[58],
                    "trregion":row[59]                                         
                }
                breaker_list.append(result)
            assets['breakers']=breaker_list

            isolator_list=[]
            for row in isolators:
                result = {
                    "switchgearno": row[0],
                    "switchgearid": row[1],
                    "type": row[2] ,
                    "voltagerating":row[3],
                    "make":row[4],
                    "depot": row[5],
                    "district":row[6],
                    "region":row[7],
                    "assetno":row[8],
                    "createdon": row[9],
                    "createdby": row[10],
                    "modifiedon": row[11],
                    "modifiedby":row[12],
                    "comments":row[13],
                    "status":row[14],
                    "districtid":row[15],
                    "wardid":row[16],
                    "provinceid":row[17],
                    "id":row[18],
                    "serialno":row[19],
                    "model":row[20],
                    "constructiontype": row[21],
                    "mco":row[22],
                    "opmech": row[23],
                    "busbarsno":row[24],
                    "optype": row[25],
                    "standard":row[26],
                    "insulationmedium": row[27],
                    "interruptingmedium":row[28],
                    "ratedcc":row[29],
                    "ratedscbc":row[30],
                    "ratedmc":row[31],
                    "ratedscwt":row[32],
                    "ratedstwc":row[33],
                    "controlvoltage":row[34],
                    "motorost":row[35],
                    "motorvoltage":row[36],
                    "auxvoltage":row[37],
                    "possiblecountsetting":row[38],
                    "autoreclosingtype":row[39],
                    "dutycycle":row[40],
                    "netmass":row[41],
                    "ocinstalled":row[42],
                    "bil":row[43],
                    "commissionyear":row[44],
                    "installationyear":row[45],
                    "baytype": row[46],
                    "use":row[47],
                    "tripcoilsno":row[48],
                    "normalopstatus": row[49],
                    "cdpoint":row[50],
                    "feedercode":row[51],
                    "geom2d": row[52],
                    "mvboard":row[53],
                    "geom3d":row[54],
                    "nostatus":row[55],
                    "manufactureyear":row[56],
                    "installed_on":row[57],
                    "asset_change":row[58],
                    "trregion":row[59]                                     
                }
                isolator_list.append(result)
            assets['isolators']=isolator_list
        return assets


    def station_transformers(self, parent_assetid):
        with connection.cursor() as cursor:

            cursor.callproc(
            'core.stationtransformers_fx', [parent_assetid])
            transformers = cursor.fetchall()
            transformer_list=[]
            for row in transformers:
                result = {
                   "transformerid": row[0],
                    "name": row[1],
                    "voltageratio": row[2],
                    "sscode": row[3],
                    "depot" :row[4] ,
                    "district":row[5], 
                    "region": row[6],
                    "assetno":row[7],
                    "createdon": row[8],
                    "createdby": row[9],
                    "modifiedon": row[10],
                    "modifiedby": row[11],
                    "comments": row[12],
                    "status": row[13],
                    "districtid": row[14],
                    "wardid": row[15],
                    "provinceid": row[16],
                    "id": row[17],
                    "serialno": row[18],
                    "systemno": row[19],
                    "highvoltage":row[20],
                    "lowvoltage":row[21],
                    "application": row[22],
                    "mounting": row[23],
                    "standard": row[24],
                    "make": row[25],
                    "transformerinsulation": row[26],
                    "manufactureryear":row[27],
                    "installationyear": row[28],
                    "commissionyear": row[29],
                    "windingsno": row[30],
                    "bil": row[31],
                    "mass": row[32],
                    "vectorgroup": row[33],
                    "impedance":row[34],
                    "ironlosses": row[35],
                    "copperlosses": row[36],
                    "taperange": row[37],
                    "cooling": row[38],
                    "capacity": row[39],
                    "geom2d": row[40],
                    "maxcapacity": row[41],
                    "windings": row[42],
                    "geom3d": row[43],
                    "asset_change": row[44],
                    "trregion": row[45],                  
                }

                transformer_list.append(result) 
        return transformer_list


    def station_feeders(self, parent_assetid):
        with connection.cursor() as cursor:            

            cursor.callproc(
            'core.stationfeeders_fx', [parent_assetid])
            feeders = cursor.fetchall()
            feeder_list=[]
            for row in feeders:
                result = {
                    "feedercode": row[0],
                    "name": row[1],
                    "voltagelevel": row[2] ,
                    "depot":row[3],
                    "district": row[4],
                    "region":row[5],
                    "assetno":row[6],
                    "createdon": row[7],
                    "createdby": row[8],
                    "modifiedon":row[9],
                    "feederno":row[10],
                    "modifiedby":row[11],
                    "comments":row[12],
                    "status":row[13],
                    "districtid":row[14],
                    "wardid":row[15],
                    "provinceid":row[16],
                    "id":row[17],
                    "geom2d": row[18],
                    "sourcesscode":row[19],
                    "asset_change":row[20],
                    "trregion":row[21]                                     
                }
                feeder_list.append(result)
            return feeder_list

    def station_switchgear_breakers(self, parent_assetid):
        with connection.cursor() as cursor:          
            cursor.callproc(
            'core.stationswitchgears_breakers_fx', [parent_assetid])
            breakers = cursor.fetchall()
            breaker_list=[]
            for row in breakers:
                result = {
                    "switchgearno": row[0],
                    "switchgearid": row[1],
                    "type": row[2] ,
                    "voltagerating":row[3],
                    "make":row[4],
                    "depot": row[5],
                    "district":row[6],
                    "region":row[7],
                    "assetno":row[8],
                    "createdon": row[9],
                    "createdby": row[10],
                    "modifiedon": row[11],
                    "modifiedby":row[12],
                    "comments":row[13],
                    "status":row[14],
                    "districtid":row[15],
                    "wardid":row[16],
                    "provinceid":row[17],
                    "id":row[18],
                    "serialno":row[19],
                    "model":row[20],
                    "constructiontype": row[21],
                    "mco":row[22],
                    "opmech": row[23],
                    "busbarsno":row[24],
                    "optype": row[25],
                    "standard":row[26],
                    "insulationmedium": row[27],
                    "interruptingmedium":row[28],
                    "ratedcc":row[29],
                    "ratedscbc":row[30],
                    "ratedmc":row[31],
                    "ratedscwt":row[32],
                    "ratedstwc":row[33],
                    "controlvoltage":row[34],
                    "motorost":row[35],
                    "motorvoltage":row[36],
                    "auxvoltage":row[37],
                    "possiblecountsetting":row[38],
                    "autoreclosingtype":row[39],
                    "dutycycle":row[40],
                    "netmass":row[41],
                    "ocinstalled":row[42],
                    "bil":row[43],
                    "commissionyear":row[44],
                    "installationyear":row[45],
                    "baytype": row[46],
                    "use":row[47],
                    "tripcoilsno":row[48],
                    "normalopstatus": row[49],
                    "cdpoint":row[50],
                    "feedercode":row[51],
                    "geom2d": row[52],
                    "mvboard":row[53],
                    "geom3d":row[54],
                    "nostatus":row[55],
                    "manufactureyear":row[56],
                    "installed_on":row[57],
                    "asset_change":row[58],
                    "trregion":row[59]                                   
                }
                breaker_list.append(result)
            return breaker_list

    def station_switchgear_isolators(self, parent_assetid):
        with connection.cursor() as cursor:   
            cursor.callproc(
            'core.stationswitchgear_isolators_fx', [parent_assetid])
            isolators = cursor.fetchall()
            isolator_list=[]
            for row in isolators:
                result = {
                     "switchgearno": row[0],
                    "switchgearid": row[1],
                    "type": row[2] ,
                    "voltagerating":row[3],
                    "make":row[4],
                    "depot": row[5],
                    "district":row[6],
                    "region":row[7],
                    "assetno":row[8],
                    "createdon": row[9],
                    "createdby": row[10],
                    "modifiedon": row[11],
                    "modifiedby":row[12],
                    "comments":row[13],
                    "status":row[14],
                    "districtid":row[15],
                    "wardid":row[16],
                    "provinceid":row[17],
                    "id":row[18],
                    "serialno":row[19],
                    "model":row[20],
                    "constructiontype": row[21],
                    "mco":row[22],
                    "opmech": row[23],
                    "busbarsno":row[24],
                    "optype": row[25],
                    "standard":row[26],
                    "insulationmedium": row[27],
                    "interruptingmedium":row[28],
                    "ratedcc":row[29],
                    "ratedscbc":row[30],
                    "ratedmc":row[31],
                    "ratedscwt":row[32],
                    "ratedstwc":row[33],
                    "controlvoltage":row[34],
                    "motorost":row[35],
                    "motorvoltage":row[36],
                    "auxvoltage":row[37],
                    "possiblecountsetting":row[38],
                    "autoreclosingtype":row[39],
                    "dutycycle":row[40],
                    "netmass":row[41],
                    "ocinstalled":row[42],
                    "bil":row[43],
                    "commissionyear":row[44],
                    "installationyear":row[45],
                    "baytype": row[46],
                    "use":row[47],
                    "tripcoilsno":row[48],
                    "normalopstatus": row[49],
                    "cdpoint":row[50],
                    "feedercode":row[51],
                    "geom2d": row[52],
                    "mvboard":row[53],
                    "geom3d":row[54],
                    "nostatus":row[55],
                    "manufactureyear":row[56],
                    "installed_on":row[57],
                    "asset_change":row[58],
                    "trregion":row[59]                                     
                }
                isolator_list.append(result)
            return isolator_list
    