/*
PostgreSQL Backup
Database: beops/core
Backup Time: 2020-03-17 17:34:50
*/

CREATE TABLE "boqlabour" (
  "boq_labour_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "e117_id" varchar(100) COLLATE "pg_catalog"."default",
  "labour_class" varchar(100) COLLATE "pg_catalog"."default",
  "number_of_people" varchar(100) COLLATE "pg_catalog"."default",
  "man_hours" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "boqlabour" OWNER TO "postgres";
CREATE TABLE "boqmaterial" (
  "boq_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "e117_id" varchar(100) COLLATE "pg_catalog"."default",
  "material" varchar(100) COLLATE "pg_catalog"."default",
  "quantity" varchar(100) COLLATE "pg_catalog"."default",
  "unit_of_measure" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "boqmaterial" OWNER TO "postgres";
CREATE TABLE "boqvehicle" (
  "boq_vehicle_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "e117_id" varchar(100) COLLATE "pg_catalog"."default",
  "vehicle_type" varchar(100) COLLATE "pg_catalog"."default",
  "no_of_vehicles" varchar(100) COLLATE "pg_catalog"."default",
  "distance" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "boqvehicle" OWNER TO "postgres";
CREATE TABLE "centre" (
  "centre_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "centre_code" varchar(100) COLLATE "pg_catalog"."default",
  "centre_name" varchar(100) COLLATE "pg_catalog"."default",
  "cost_centre" varchar(100) COLLATE "pg_catalog"."default",
  "type" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "centre" OWNER TO "bedjango";
CREATE TABLE "common" (
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
;
ALTER TABLE "common" OWNER TO "postgres";
CREATE TABLE "django_admin_log" (
  "id" int4 NOT NULL DEFAULT nextval('core.django_admin_log_id_seq'::regclass),
  "action_time" timestamptz(6) NOT NULL,
  "object_id" text COLLATE "pg_catalog"."default",
  "object_repr" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "action_flag" int2 NOT NULL,
  "change_message" text COLLATE "pg_catalog"."default" NOT NULL,
  "content_type_id" int4,
  "user_id" int4 NOT NULL
)
;
ALTER TABLE "django_admin_log" OWNER TO "bedjango";
CREATE TABLE "django_content_type" (
  "id" int4 NOT NULL DEFAULT nextval('core.django_content_type_id_seq'::regclass),
  "app_label" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "model" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "django_content_type" OWNER TO "bedjango";
CREATE TABLE "django_migrations" (
  "id" int4 NOT NULL DEFAULT nextval('core.django_migrations_id_seq'::regclass),
  "app" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "applied" timestamptz(6) NOT NULL
)
;
ALTER TABLE "django_migrations" OWNER TO "bedjango";
CREATE TABLE "django_session" (
  "session_key" varchar(40) COLLATE "pg_catalog"."default" NOT NULL,
  "session_data" text COLLATE "pg_catalog"."default" NOT NULL,
  "expire_date" timestamptz(6) NOT NULL
)
;
ALTER TABLE "django_session" OWNER TO "bedjango";
CREATE TABLE "e117" (
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now(),
  "e117_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "client_inspection_type" varchar(250) COLLATE "pg_catalog"."default",
  "e117client_id" varchar(250) COLLATE "pg_catalog"."default",
  "client_contractor_name" varchar(250) COLLATE "pg_catalog"."default",
  "client_contractor_address" varchar(250) COLLATE "pg_catalog"."default",
  "client_contractor_phone" varchar(250) COLLATE "pg_catalog"."default",
  "soi_size" int4,
  "soi_voltage" int4,
  "soi_conduit" int4,
  "soi_switch_type" varchar(250) COLLATE "pg_catalog"."default",
  "soi_switch_capacity" float8,
  "soi_switch_setting" float8,
  "insd_neutrals_fused" varchar(20) COLLATE "pg_catalog"."default",
  "insd_neutrals_fused_cmt" text COLLATE "pg_catalog"."default",
  "insd_block_fitted" varchar(20) COLLATE "pg_catalog"."default",
  "insd_block_fitted_cmt" text COLLATE "pg_catalog"."default",
  "insd_electrode_installed" varchar(20) COLLATE "pg_catalog"."default",
  "insd_electrode_installed_cmt" text COLLATE "pg_catalog"."default",
  "insd_electrode_type" varchar(250) COLLATE "pg_catalog"."default",
  "insd_bonded_earth" varchar(20) COLLATE "pg_catalog"."default",
  "insd_bonded_earth_cmt" text COLLATE "pg_catalog"."default",
  "insd_polarity_switches" varchar(250) COLLATE "pg_catalog"."default",
  "insd_outlets_earthed" varchar(20) COLLATE "pg_catalog"."default",
  "insd_outlets_earthed_cmt" text COLLATE "pg_catalog"."default",
  "insd_socket_outlets" varchar(250) COLLATE "pg_catalog"."default",
  "insd_type_wiring" varchar(250) COLLATE "pg_catalog"."default",
  "insd_conductors_size" varchar(20) COLLATE "pg_catalog"."default",
  "insd_conductors_size_cmt" text COLLATE "pg_catalog"."default",
  "insd_condition_wiring" varchar(20) COLLATE "pg_catalog"."default",
  "insd_condition_wiring_cmt" text COLLATE "pg_catalog"."default",
  "insd_cord_positions" varchar(250) COLLATE "pg_catalog"."default",
  "insd_bathroom_switch" varchar(20) COLLATE "pg_catalog"."default",
  "insd_bathroom_switch_cmt" text COLLATE "pg_catalog"."default",
  "insd_unearthed_metalclad" varchar(250) COLLATE "pg_catalog"."default",
  "inst_megger_ln" float8,
  "inst_megger_le" float8,
  "inst_megger_ne" float8,
  "inst_continuity_resistance" int4,
  "conduits_conduits_bushed" varchar(20) COLLATE "pg_catalog"."default",
  "conduits_conduits_bushed_cmt" text COLLATE "pg_catalog"."default",
  "conduits_bonded" varchar(20) COLLATE "pg_catalog"."default",
  "conduits_bonded_cmt" text COLLATE "pg_catalog"."default",
  "conduits_correct_size" varchar(20) COLLATE "pg_catalog"."default",
  "conduits_correct_size_cmt" text COLLATE "pg_catalog"."default",
  "conduits_adequately_supported" varchar(20) COLLATE "pg_catalog"."default",
  "conduits_adequately_supported_cmt" text COLLATE "pg_catalog"."default",
  "conduits_suitable_type" varchar(20) COLLATE "pg_catalog"."default",
  "conduits_suitable_type_cmt" text COLLATE "pg_catalog"."default",
  "lighting_lighting_points" int4,
  "lighting_maximum_lighting_points" int4,
  "plugs_plug_points" int4,
  "plugs_maximum_plug_points" int4,
  "appliances_number_motors" int4,
  "appliances_size_motors" int4,
  "appliances_motor_installation" varchar(20) COLLATE "pg_catalog"."default",
  "appliances_motor_installation_cmt" text COLLATE "pg_catalog"."default",
  "appliances_outbuildings_switches" varchar(20) COLLATE "pg_catalog"."default",
  "appliances_outbuildings_switches_cmt" text COLLATE "pg_catalog"."default",
  "oh_height_satisfactory" varchar(20) COLLATE "pg_catalog"."default",
  "oh_height_satisfactory_cmt" text COLLATE "pg_catalog"."default",
  "oh_support_satisfactory" varchar(20) COLLATE "pg_catalog"."default",
  "oh_support_satisfactory_cmt" text COLLATE "pg_catalog"."default",
  "oh_conductor_size" int4,
  "oh_condition_line" varchar(20) COLLATE "pg_catalog"."default",
  "oh_condition_line_cmt" text COLLATE "pg_catalog"."default",
  "oh_earthwires_fitted" varchar(20) COLLATE "pg_catalog"."default",
  "oh_earthwires_fitted_cmt" text COLLATE "pg_catalog"."default",
  "defects_installation" varchar(250) COLLATE "pg_catalog"."default",
  "defects_contractor" varchar(20) COLLATE "pg_catalog"."default",
  "defects_contractor_cmt" text COLLATE "pg_catalog"."default",
  "general_switch_details" varchar(250) COLLATE "pg_catalog"."default",
  "general_supply_status" varchar(20) COLLATE "pg_catalog"."default",
  "general_installation_status" varchar(100) COLLATE "pg_catalog"."default",
  "general_installation_status_cmt" text COLLATE "pg_catalog"."default",
  "boq_connection_duration_hr" float8,
  "datetime_completed" timestamp(6),
  "completed_by" varchar COLLATE "pg_catalog"."default",
  "designation" varchar COLLATE "pg_catalog"."default"
)
INHERITS ("core"."common")
;
ALTER TABLE "e117" OWNER TO "postgres";
CREATE TABLE "e117client" (
  "client_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "client_name" varchar(100) COLLATE "pg_catalog"."default",
  "property_address" varchar(100) COLLATE "pg_catalog"."default",
  "client_phone" varchar(100) COLLATE "pg_catalog"."default",
  "geom" "public"."geometry",
  "owner_name" varchar(100) COLLATE "pg_catalog"."default",
  "owner_address" varchar COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "e117client" OWNER TO "postgres";
CREATE TABLE "e117equipment" (
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now(),
  "equipment_id" varchar(250) COLLATE "pg_catalog"."default" NOT NULL,
  "e117_id" varchar(250) COLLATE "pg_catalog"."default",
  "description" varchar(250) COLLATE "pg_catalog"."default",
  "wattage" float8
)
INHERITS ("core"."common")
;
ALTER TABLE "e117equipment" OWNER TO "postgres";
CREATE TABLE "e50autodisconnect" (
  "auto_disconect_id " varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "switch_number" varchar(100) COLLATE "pg_catalog"."default",
  "type" varchar(100) COLLATE "pg_catalog"."default",
  "mechanism_operation" varchar(100) COLLATE "pg_catalog"."default",
  "bush_condition" varchar(100) COLLATE "pg_catalog"."default",
  "earthing_intact" varchar(100) COLLATE "pg_catalog"."default",
  "tripping_circuit" varchar(100) COLLATE "pg_catalog"."default",
  "comments" text COLLATE "pg_catalog"."default",
  "section_completed" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e50autodisconnect" OWNER TO "postgres";
CREATE TABLE "e50controlcubicle" (
  "control_cubicle_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "clean_relays_operate" varchar(100) COLLATE "pg_catalog"."default",
  "fuses_links_position" varchar(100) COLLATE "pg_catalog"."default",
  "lamps_indicating" varchar(100) COLLATE "pg_catalog"."default",
  "clean_panel_wiring_inorder" varchar(100) COLLATE "pg_catalog"."default",
  "cubicle_lights_heaters" varchar(100) COLLATE "pg_catalog"."default",
  "comments" text COLLATE "pg_catalog"."default",
  "section_completed" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e50controlcubicle" OWNER TO "postgres";
CREATE TABLE "e50feeder" (
  "e50_feeder_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "feeder_id" varchar(100) COLLATE "pg_catalog"."default",
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "indicated_red_phase(amps)" varchar(100) COLLATE "pg_catalog"."default",
  "indicated_yellow_phase" varchar(100) COLLATE "pg_catalog"."default",
  "indicated_blue_phase" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e50feeder" OWNER TO "postgres";
CREATE TABLE "e50general" (
  "general_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "district" varchar(100) COLLATE "pg_catalog"."default",
  "substation_name" varchar(100) COLLATE "pg_catalog"."default",
  "substation_number" varchar(100) COLLATE "pg_catalog"."default",
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "insulators_arrestors" varchar(100) COLLATE "pg_catalog"."default",
  "dfuse_isolators" varchar(100) COLLATE "pg_catalog"."default",
  "busbars_jumpers" varchar(100) COLLATE "pg_catalog"."default",
  "s/s_earth_date_tested" timestamptz(6),
  "earthing_structure" varchar(100) COLLATE "pg_catalog"."default",
  "fire_equipment_expiry_date" timestamptz(6),
  "cables_boxes_glands" varchar(100) COLLATE "pg_catalog"."default",
  "substation_surround" varchar(100) COLLATE "pg_catalog"."default",
  "paintwork_condition" varchar(100) COLLATE "pg_catalog"."default",
  "comments" text COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "overall_result" varchar(100) COLLATE "pg_catalog"."default",
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e50general" OWNER TO "postgres";
CREATE TABLE "e50protectioncubicle" (
  "protection_cubicle_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "relay_satisf_flag_reset" varchar(100) COLLATE "pg_catalog"."default",
  "sef_uniselector_reset" varchar(100) COLLATE "pg_catalog"."default",
  "fuses_links_position" varchar(100) COLLATE "pg_catalog"."default",
  "clean_panel_wiring_inorder" varchar(100) COLLATE "pg_catalog"."default",
  "float_voltage" varchar(100) COLLATE "pg_catalog"."default",
  "charger_current" varchar(100) COLLATE "pg_catalog"."default",
  "switch_off_charger" varchar(100) COLLATE "pg_catalog"."default",
  "battery_voltage" varchar(100) COLLATE "pg_catalog"."default",
  "min_cell_voltage" varchar(100) COLLATE "pg_catalog"."default",
  "load_test" varchar(100) COLLATE "pg_catalog"."default",
  "top_up_cells" varchar(100) COLLATE "pg_catalog"."default",
  "clean_terminal" varchar(100) COLLATE "pg_catalog"."default",
  "terminal_connections" varchar(100) COLLATE "pg_catalog"."default",
  "switch_on_charger" varchar(100) COLLATE "pg_catalog"."default",
  "cubicle_lights_heaters" varchar(100) COLLATE "pg_catalog"."default",
  "comments" varchar(100) COLLATE "pg_catalog"."default",
  "section_completed" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e50protectioncubicle" OWNER TO "postgres";
CREATE TABLE "e50switchgear" (
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "switch_number" varchar(100) COLLATE "pg_catalog"."default",
  "present_counter_readings" varchar(100) COLLATE "pg_catalog"."default",
  "last_overhaul_counter_reading" varchar(100) COLLATE "pg_catalog"."default",
  "number_operations" varchar(100) COLLATE "pg_catalog"."default",
  "date_oil_changed" timestamptz(6),
  "bushing_condition" varchar(100) COLLATE "pg_catalog"."default",
  "oil_leaks" varchar(100) COLLATE "pg_catalog"."default",
  "earthing_intact" varchar(100) COLLATE "pg_catalog"."default",
  "tripping_circuit" varchar(100) COLLATE "pg_catalog"."default",
  "comments" text COLLATE "pg_catalog"."default",
  "section_completed" varchar(100) COLLATE "pg_catalog"."default",
  "e50_switch_gear_id" varchar(100) COLLATE "pg_catalog"."default",
  "switch_gear_id" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e50switchgear" OWNER TO "postgres";
CREATE TABLE "e60dfuses" (
  "dfuses_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "state" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "rating_type" varchar(100) COLLATE "pg_catalog"."default",
  "gauze_washers" varchar(100) COLLATE "pg_catalog"."default",
  "holders_drop" varchar(100) COLLATE "pg_catalog"."default",
  "holders_contact" varchar(100) COLLATE "pg_catalog"."default",
  "contacts_dressing_treated" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60dfuses" OWNER TO "postgres";
CREATE TABLE "e60lightningarrester" (
  "e60lightningarrester_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "state" varchar(100) COLLATE "pg_catalog"."default",
  "lightning_arrester_id" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "make_type" varchar(100) COLLATE "pg_catalog"."default",
  "voltage_rating" varchar(100) COLLATE "pg_catalog"."default",
  "connected_landslide" varchar(100) COLLATE "pg_catalog"."default",
  "arrester_rail_conected" varchar(100) COLLATE "pg_catalog"."default",
  "capacitor_satisfactory" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60lightningarrester" OWNER TO "postgres";
CREATE TABLE "e60meter" (
  "e60_id " varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "substation_meter_id " varchar(100) COLLATE "pg_catalog"."default",
  "state" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60meter" OWNER TO "postgres";
CREATE TABLE "e60meterswitchgearhousing" (
  "meterswitchgear_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "state" varchar(100) COLLATE "pg_catalog"."default",
  "type(cubicle_house)" varchar(100) COLLATE "pg_catalog"."default",
  "housing_weatherproof" varchar(100) COLLATE "pg_catalog"."default",
  "weatherproof_door" varchar(100) COLLATE "pg_catalog"."default",
  "paintwork_condition" varchar(100) COLLATE "pg_catalog"."default",
  "water_outlet" varchar(100) COLLATE "pg_catalog"."default",
  "door_padlocks" varchar(100) COLLATE "pg_catalog"."default",
  "lubricated_padlock" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60meterswitchgearhousing" OWNER TO "postgres";
CREATE TABLE "e60substationgeneral" (
  "SubstationGeneral_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "earth_resistance" varchar(100) COLLATE "pg_catalog"."default",
  "number_earthrodes" varchar(100) COLLATE "pg_catalog"."default",
  "all_bonded" varchar(100) COLLATE "pg_catalog"."default",
  "l.tcable_conduit_bonded" varchar(100) COLLATE "pg_catalog"."default",
  "l.tmains_conditions" varchar(100) COLLATE "pg_catalog"."default",
  "pole_condition" varchar(100) COLLATE "pg_catalog"."default",
  "paintwork_condition" varchar(100) COLLATE "pg_catalog"."default",
  "site_clear_undergrowth" varchar(100) COLLATE "pg_catalog"."default",
  "site_accessible" varchar(100) COLLATE "pg_catalog"."default",
  "lt_mains_type_length" varchar(100) COLLATE "pg_catalog"."default",
  "remarks" varchar(100) COLLATE "pg_catalog"."default",
  "station_id" varchar(100) COLLATE "pg_catalog"."default",
  "work_order_number" varchar(100) COLLATE "pg_catalog"."default",
  "section" varchar(100) COLLATE "pg_catalog"."default",
  "substation_structure" varchar(100) COLLATE "pg_catalog"."default",
  "construction_type" varchar(100) COLLATE "pg_catalog"."default",
  "pole_type" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60substationgeneral" OWNER TO "postgres";
CREATE TABLE "e60switchgear" (
  "e60switchgear_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "switch_gear_id" varchar(100) COLLATE "pg_catalog"."default",
  "state" varchar(100) COLLATE "pg_catalog"."default",
  "form_completed" varchar(100) COLLATE "pg_catalog"."default",
  "trip_setting" varchar(100) COLLATE "pg_catalog"."default",
  "oil_condition" varchar(100) COLLATE "pg_catalog"."default",
  "contacts_condition" varchar(100) COLLATE "pg_catalog"."default",
  "dash_pots" varchar(100) COLLATE "pg_catalog"."default",
  "nuts_connection" varchar(100) COLLATE "pg_catalog"."default",
  "consumer_trip_setting" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60switchgear" OWNER TO "postgres";
CREATE TABLE "e60transformer" (
  "e60_transformer_id " varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "transformer_id_fk " varchar(100) COLLATE "pg_catalog"."default",
  "state  " varchar(100) COLLATE "pg_catalog"."default",
  "form_completed " varchar(100) COLLATE "pg_catalog"."default",
  "mounting_security" varchar(100) COLLATE "pg_catalog"."default",
  "tank_bond" varchar(100) COLLATE "pg_catalog"."default",
  "l.t_neutral_bond" varchar(100) COLLATE "pg_catalog"."default",
  "bushings" varchar(100) COLLATE "pg_catalog"."default",
  "paintwork" varchar(100) COLLATE "pg_catalog"."default",
  "arcing_horn" varchar(100) COLLATE "pg_catalog"."default",
  "breather_type" varchar(100) COLLATE "pg_catalog"."default",
  "breather_condition" varchar(100) COLLATE "pg_catalog"."default",
  "oil_leaks" varchar(100) COLLATE "pg_catalog"."default",
  "megger_HT-E" varchar(100) COLLATE "pg_catalog"."default",
  "megger_LT-E" varchar(100) COLLATE "pg_catalog"."default",
  "megger_HT-LT" varchar(100) COLLATE "pg_catalog"."default",
  "megger_HT-LT/E" varchar(100) COLLATE "pg_catalog"."default",
  "megger_oil_temperature" varchar(100) COLLATE "pg_catalog"."default",
  "oil_test_results" varchar(100) COLLATE "pg_catalog"."default",
  "tap_range_tap_position" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e60transformer" OWNER TO "postgres";
CREATE TABLE "e84general" (
  "e84_general_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "district" varchar(100) COLLATE "pg_catalog"."default",
  "section_number" varchar(100) COLLATE "pg_catalog"."default",
  "construction_type" varchar(100) COLLATE "pg_catalog"."default",
  "comment" text COLLATE "pg_catalog"."default",
  "overall_result" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "rowid" int4,
  "sync_status" int4,
  "section_length" numeric(20,2),
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "e84general" OWNER TO "postgres";
CREATE TABLE "e84lineinspection" (
  "line_inspection_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "pole_number" varchar(100) COLLATE "pg_catalog"."default",
  "pole_type" varchar(100) COLLATE "pg_catalog"."default",
  "wayleave" varchar(100) COLLATE "pg_catalog"."default",
  "comment" varchar(100) COLLATE "pg_catalog"."default",
  "cross_arm" varchar(100) COLLATE "pg_catalog"."default",
  "insulator" varchar(100) COLLATE "pg_catalog"."default",
  "conductors" varchar(100) COLLATE "pg_catalog"."default",
  "stays" varchar(100) COLLATE "pg_catalog"."default",
  "earthing" varchar(100) COLLATE "pg_catalog"."default",
  "cradles" varchar(100) COLLATE "pg_catalog"."default",
  "anti_climbing_device" varchar(100) COLLATE "pg_catalog"."default",
  "created_by" varchar(100) COLLATE "pg_catalog"."default",
  "created_on" timestamp(6),
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "rowid" int4,
  "sync_status" int4,
  "e84_general_id" varchar(100) COLLATE "pg_catalog"."default",
  "pole" varchar(100) COLLATE "pg_catalog"."default",
  "pole_material" varchar(100) COLLATE "pg_catalog"."default",
  "voltage_level" varchar(100) COLLATE "pg_catalog"."default",
  "point" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "e84lineinspection" OWNER TO "postgres";
CREATE TABLE "feeder" (
  "feeder_id_pk" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(100) COLLATE "pg_catalog"."default",
  "equipment_id" varchar(100) COLLATE "pg_catalog"."default",
  "voltage" varchar(100) COLLATE "pg_catalog"."default",
  "feeder_number" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "feeder" OWNER TO "postgres";
CREATE TABLE "fleetprogress" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
),
  "fleet_no" varchar(100) COLLATE "pg_catalog"."default",
  "trip_date" date,
  "point" varchar(255) COLLATE "pg_catalog"."default",
  "starting_mileage" int8,
  "ending_mileage" int8,
  "job_progress_id" varchar(255) COLLATE "pg_catalog"."default",
  "assigned_to" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "created_on" date,
  "created_by" varchar(255) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "fleetprogress" OWNER TO "bedjango";
CREATE TABLE "job" (
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "job_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "work_order_id" varchar(100) COLLATE "pg_catalog"."default",
  "type" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default",
  "asset_id" varchar(100) COLLATE "pg_catalog"."default",
  "assignee" varchar(100) COLLATE "pg_catalog"."default",
  "comments" text COLLATE "pg_catalog"."default",
  "closed_by" varchar(100) COLLATE "pg_catalog"."default",
  "closed_dt" timestamp(6),
  "asset_name" varchar(100) COLLATE "pg_catalog"."default",
  "asset_type" varchar(100) COLLATE "pg_catalog"."default",
  "asset_number" varchar(100) COLLATE "pg_catalog"."default",
  "expected_end_dt" date,
  "reference_no" varchar(100) COLLATE "pg_catalog"."default",
  "asset_serial" varchar(100) COLLATE "pg_catalog"."default",
  "workflow_id" varchar(100) COLLATE "pg_catalog"."default",
  "rowid" int4,
  "rowversion" int4,
  "sync_status" int4 DEFAULT 0,
  "status" int4 NOT NULL,
  "geom" text COLLATE "pg_catalog"."default",
  "trigger" varchar(100) COLLATE "pg_catalog"."default",
  "start_date" date,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "job" OWNER TO "postgres";
CREATE TABLE "jobattachment" (
  "job_attach_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "comments" varchar(100) COLLATE "pg_catalog"."default",
  "attachment" bytea,
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "jobattachment" OWNER TO "postgres";
CREATE TABLE "jobprogress" (
  "job_progress_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "start_dt" timestamp(6),
  "end_dt" timestamp(6),
  "fleet_no" varchar(100) COLLATE "pg_catalog"."default",
  "open_mileage" int4,
  "close_mileage" int4,
  "geom_start" text COLLATE "pg_catalog"."default",
  "geom_end" text COLLATE "pg_catalog"."default",
  "comments" text COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "rowid" int4,
  "sync_status" int4,
  "status" int4,
  "action" int4,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "jobprogress" OWNER TO "postgres";
CREATE TABLE "jobstatus" (
  "job_status_id" int4 NOT NULL,
  "status" varchar(100) COLLATE "pg_catalog"."default",
  "status1" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "jobstatus" OWNER TO "postgres";
CREATE TABLE "jobteam" (
  "job_team_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "job_progress_id" varchar(100) COLLATE "pg_catalog"."default",
  "ec_num" varchar(100) COLLATE "pg_catalog"."default",
  "start_dt" varchar(100) COLLATE "pg_catalog"."default",
  "end_dt" varchar(100) COLLATE "pg_catalog"."default",
  "teamleader" varchar(100) COLLATE "pg_catalog"."default",
  "description" varchar(100) COLLATE "pg_catalog"."default",
  "created_by" varchar(100) COLLATE "pg_catalog"."default",
  "created_on" timestamp(6),
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "rowid" int4,
  "sync_status" int4
)
;
ALTER TABLE "jobteam" OWNER TO "postgres";
CREATE TABLE "jobtype" (
  "job_type_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "type" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "jobtype" OWNER TO "postgres";
CREATE TABLE "lightningarrester" (
  "lightning_arrester_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "make" varchar(100) COLLATE "pg_catalog"."default",
  "voltage_rating" varchar(100) COLLATE "pg_catalog"."default",
  "ltype" varchar(100) COLLATE "pg_catalog"."default",
  "kvar_rating" varchar(100) COLLATE "pg_catalog"."default",
  "job_id" varchar(100) COLLATE "pg_catalog"."default",
  "installed_on" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "lightningarrester" OWNER TO "postgres";
CREATE TABLE "pole" (
  "pole_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "equipment_id" varchar(100) COLLATE "pg_catalog"."default",
  "pole_no" varchar(100) COLLATE "pg_catalog"."default",
  "pole_type" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "pole" OWNER TO "postgres";
CREATE TABLE "substationmeter" (
  "meter_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "meter_no" varchar(100) COLLATE "pg_catalog"."default",
  "equipment_id" varchar(100) COLLATE "pg_catalog"."default",
  "make" varchar(100) COLLATE "pg_catalog"."default",
  "amps" varchar(100) COLLATE "pg_catalog"."default",
  "volts" varchar(100) COLLATE "pg_catalog"."default",
  "voltage" varchar(100) COLLATE "pg_catalog"."default",
  "maker_type" varchar(100) COLLATE "pg_catalog"."default",
  "maker_serial_number" varchar(100) COLLATE "pg_catalog"."default",
  "zetdc_number" varchar(100) COLLATE "pg_catalog"."default",
  "vad_transformer_zetdc_number" varchar(100) COLLATE "pg_catalog"."default",
  "ct_ratio" varchar(100) COLLATE "pg_catalog"."default",
  "meter_protection_type" varchar(100) COLLATE "pg_catalog"."default",
  "constant_rx" varchar(100) COLLATE "pg_catalog"."default",
  "feeder_id " varchar(100) COLLATE "pg_catalog"."default",
  "status" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "substationmeter" OWNER TO "postgres";
CREATE TABLE "switchgear" (
  "switchgear_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "swtype" varchar(100) COLLATE "pg_catalog"."default",
  "equipment_id" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "switchgear" OWNER TO "postgres";
CREATE TABLE "team" (
  "team_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "team_leader" varchar(100) COLLATE "pg_catalog"."default",
  "team_member" varchar(100) COLLATE "pg_catalog"."default",
  "specialisation" varchar(100) COLLATE "pg_catalog"."default",
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "team" OWNER TO "postgres";
CREATE TABLE "teamleader" (
  "team_leader" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "specialisation" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "teamleader" OWNER TO "postgres";
CREATE TABLE "transformer" (
  "transformer_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "make" varchar(100) COLLATE "pg_catalog"."default",
  "equipment_id" varchar(100) COLLATE "pg_catalog"."default",
  "voltage_ratio" varchar(100) COLLATE "pg_catalog"."default",
  "rating" varchar(100) COLLATE "pg_catalog"."default",
  "status" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "transformer" OWNER TO "postgres";
CREATE TABLE "workorder" (
  "created_by" varchar(100) COLLATE "pg_catalog"."default" DEFAULT CURRENT_USER,
  "modified_by" varchar(100) COLLATE "pg_catalog"."default",
  "modified_on" timestamp(6),
  "work_order_id" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "description" varchar(100) COLLATE "pg_catalog"."default",
  "centre" varchar(100) COLLATE "pg_catalog"."default",
  "comments" varchar(100) COLLATE "pg_catalog"."default",
  "status" int4,
  "created_on" timestamp(6) DEFAULT now()
)
INHERITS ("core"."common")
;
ALTER TABLE "workorder" OWNER TO "postgres";
ALTER TABLE "boqlabour" ADD CONSTRAINT "boqLabour_pkey" PRIMARY KEY ("boq_labour_id");
CREATE INDEX "fki_boqlabour_e117_id" ON "boqlabour" USING btree (
  "e117_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "boqmaterial" ADD CONSTRAINT "boqMaterials_pkey" PRIMARY KEY ("boq_id");
CREATE INDEX "fki_boqmaterial_e117_id" ON "boqmaterial" USING btree (
  "e117_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "boqvehicle" ADD CONSTRAINT "boqVehicle_pkey" PRIMARY KEY ("boq_vehicle_id");
CREATE INDEX "fki_boqvehicle_client_id" ON "boqvehicle" USING btree (
  "e117_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "centre" ADD CONSTRAINT "centre_pkey" PRIMARY KEY ("centre_id");
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_pkey" PRIMARY KEY ("id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" USING btree (
  "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id");
ALTER TABLE "django_migrations" ADD CONSTRAINT "django_migrations_pkey" PRIMARY KEY ("id");
ALTER TABLE "django_session" ADD CONSTRAINT "django_session_pkey" PRIMARY KEY ("session_key");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" USING btree (
  "expire_date" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);
CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" USING btree (
  "session_key" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);
ALTER TABLE "e117" ADD CONSTRAINT "e117_id_pk" PRIMARY KEY ("e117_id");
CREATE INDEX "fki_e117_job_id_fk" ON "e117" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "fki_e117client_id_fk" ON "e117" USING btree (
  "e117client_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e117client" ADD CONSTRAINT "client_pkey" PRIMARY KEY ("client_id");
ALTER TABLE "e117equipment" ADD CONSTRAINT "e117equipment_id_pk" PRIMARY KEY ("equipment_id");
CREATE INDEX "fki_e117equipment_id_fk" ON "e117equipment" USING btree (
  "e117_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e50autodisconnect" ADD CONSTRAINT "autoDisconnect_pkey" PRIMARY KEY ("auto_disconect_id ");
CREATE INDEX "fki_job_auto_disconnect_id_fk" ON "e50autodisconnect" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e50controlcubicle" ADD CONSTRAINT "controlCubicle_pkey" PRIMARY KEY ("control_cubicle_id");
CREATE INDEX "fki_job_control_cubicle_fk" ON "e50controlcubicle" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e50feeder" ADD CONSTRAINT "feeder__id_pkey" PRIMARY KEY ("e50_feeder_id");
CREATE INDEX "fki_feeder_id_fk" ON "e50feeder" USING btree (
  "feeder_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "fki_job_feeder_fk" ON "e50feeder" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e50general" ADD CONSTRAINT "general_id_pkey" PRIMARY KEY ("general_id");
CREATE INDEX "fki_job_e50_fk" ON "e50general" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e50protectioncubicle" ADD CONSTRAINT "protectionCubicle_pkey" PRIMARY KEY ("protection_cubicle_id");
CREATE INDEX "fki_job_protection_cubicle_fk" ON "e50protectioncubicle" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "fki_job_switch_gear_fk" ON "e50switchgear" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60dfuses" ADD CONSTRAINT "dfuses_pkey" PRIMARY KEY ("dfuses_id");
CREATE INDEX "fki_job_dfuses_id_fk" ON "e60dfuses" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60lightningarrester" ADD CONSTRAINT "lightningArrester_pkey" PRIMARY KEY ("e60lightningarrester_id");
CREATE INDEX "fki_job_lightining_arrester_id_fk" ON "e60lightningarrester" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "fki_lightningarrester_lightning_arrester_id_fk" ON "e60lightningarrester" USING btree (
  "lightning_arrester_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60meter" ADD CONSTRAINT "e60Meter_id_pkey" PRIMARY KEY ("e60_id ");
CREATE INDEX "fki_substation_substation_meter_id" ON "e60meter" USING btree (
  "substation_meter_id " COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60meterswitchgearhousing" ADD CONSTRAINT "e60MeterSwitchGear_housing_pkey" PRIMARY KEY ("meterswitchgear_id");
CREATE INDEX "fki_job_meterswitchgear_id_fk" ON "e60meterswitchgearhousing" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60substationgeneral" ADD CONSTRAINT "e60SubstationGeneral_pkey" PRIMARY KEY ("SubstationGeneral_id");
CREATE INDEX "fki_job_substation_id" ON "e60substationgeneral" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60switchgear" ADD CONSTRAINT "e60SwitchGear_pkey" PRIMARY KEY ("e60switchgear_id");
CREATE INDEX "fki_switch_gear_e60_fk" ON "e60switchgear" USING btree (
  "switch_gear_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e60transformer" ADD CONSTRAINT "e60Transformer_pkey" PRIMARY KEY ("e60_transformer_id ");
CREATE INDEX "fki_transformer_e60_fk" ON "e60transformer" USING btree (
  "transformer_id_fk " COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e84general" ADD CONSTRAINT "e84_general_id_pk" PRIMARY KEY ("e84_general_id");
CREATE INDEX "fki_e84general_job_id_fk" ON "e84general" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "e84lineinspection" ADD CONSTRAINT "line_inspection_id_pk" PRIMARY KEY ("line_inspection_id");
CREATE INDEX "fki_e84_general_id_fk" ON "e84lineinspection" USING btree (
  "e84_general_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "feeder" ADD CONSTRAINT "feeder_id_pkey" PRIMARY KEY ("feeder_id_pk");
ALTER TABLE "fleetprogress" ADD CONSTRAINT "fleet_progress_pkey" PRIMARY KEY ("id");
ALTER TABLE "job" ADD CONSTRAINT "job_job_id_pk" PRIMARY KEY ("job_id");
CREATE INDEX "fki_appflow_workflow_code_fk" ON "job" USING btree (
  "workflow_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "fki_jobstatus_fk" ON "job" USING btree (
  "status" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "fki_jobtype_fk" ON "job" USING btree (
  "type" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "fki_workOrder_work_order_id_fk" ON "job" USING btree (
  "work_order_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "jobattachment" ADD CONSTRAINT "jobAttachment_pkey" PRIMARY KEY ("job_attach_id");
CREATE INDEX "fki_job_id_fk" ON "jobattachment" USING btree (
  "job_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "jobprogress" ADD CONSTRAINT "job_progress_pkey" PRIMARY KEY ("job_progress_id");
ALTER TABLE "jobstatus" ADD CONSTRAINT "jobstatus_pkey" PRIMARY KEY ("job_status_id");
ALTER TABLE "jobteam" ADD CONSTRAINT "jobTeam_pkey" PRIMARY KEY ("job_team_id");
ALTER TABLE "jobtype" ADD CONSTRAINT "job_type_pkey" PRIMARY KEY ("job_type_id");
ALTER TABLE "lightningarrester" ADD CONSTRAINT "LigtningArrester_id_pk" PRIMARY KEY ("lightning_arrester_id");
ALTER TABLE "pole" ADD CONSTRAINT "pole_id_pkey" PRIMARY KEY ("pole_id");
ALTER TABLE "substationmeter" ADD CONSTRAINT "substation_meter_id_pkey" PRIMARY KEY ("meter_id");
CREATE INDEX "fki_feeder_feeder_id" ON "substationmeter" USING btree (
  "feeder_id " COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
ALTER TABLE "switchgear" ADD CONSTRAINT "switchGear_id_pkey" PRIMARY KEY ("switchgear_id");
ALTER TABLE "team" ADD CONSTRAINT "team_team_id_pk" PRIMARY KEY ("team_id");
ALTER TABLE "teamleader" ADD CONSTRAINT "teamleader_pkey" PRIMARY KEY ("team_leader");
CREATE INDEX "teamleader_team_leader_a13078e9_like" ON "teamleader" USING btree (
  "team_leader" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);
ALTER TABLE "transformer" ADD CONSTRAINT "transformer_id_pkey" PRIMARY KEY ("transformer_id");
ALTER TABLE "workorder" ADD CONSTRAINT "workOrder_work_order_id_pk" PRIMARY KEY ("work_order_id");
CREATE INDEX "fki_job_status_fk" ON "workorder" USING btree (
  "status" "pg_catalog"."int4_ops" ASC NULLS LAST
);
ALTER TABLE "boqlabour" ADD CONSTRAINT "boqlabour_e117_id" FOREIGN KEY ("e117_id") REFERENCES "core"."e117" ("e117_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "boqmaterial" ADD CONSTRAINT "boqmaterial_e117_id" FOREIGN KEY ("e117_id") REFERENCES "core"."e117" ("e117_id") ON DELETE NO ACTION ON UPDATE CASCADE;
ALTER TABLE "boqvehicle" ADD CONSTRAINT "boqvehicle_e117_id" FOREIGN KEY ("e117_id") REFERENCES "core"."e117" ("e117_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_action_flag_check" CHECK ((action_flag >= 0));
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "core"."django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "core"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");
ALTER TABLE "e117" ADD CONSTRAINT "e117_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e117" ADD CONSTRAINT "e117client_id_fk" FOREIGN KEY ("e117client_id") REFERENCES "core"."e117client" ("client_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e117" ADD CONSTRAINT "job_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e117equipment" ADD CONSTRAINT "e117equipment_id_fk" FOREIGN KEY ("e117_id") REFERENCES "core"."e117" ("e117_id") ON DELETE NO ACTION ON UPDATE CASCADE;
ALTER TABLE "e50autodisconnect" ADD CONSTRAINT "job_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e50controlcubicle" ADD CONSTRAINT "job_control_cubicle_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e50feeder" ADD CONSTRAINT "feeder_id_fk" FOREIGN KEY ("feeder_id") REFERENCES "core"."feeder" ("feeder_id_pk") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e50feeder" ADD CONSTRAINT "job_feeder_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e50general" ADD CONSTRAINT "job_e50_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e50protectioncubicle" ADD CONSTRAINT "job_protection_cubicle_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e50switchgear" ADD CONSTRAINT "job_switch_gear_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e60dfuses" ADD CONSTRAINT "job_dfuses_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e60lightningarrester" ADD CONSTRAINT "job_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e60lightningarrester" ADD CONSTRAINT "lightningarrester_lightning_arrester_id_fk" FOREIGN KEY ("lightning_arrester_id") REFERENCES "core"."lightningarrester" ("lightning_arrester_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e60meter" ADD CONSTRAINT "substation_substation_meter_id" FOREIGN KEY ("substation_meter_id ") REFERENCES "core"."substationmeter" ("meter_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e60meterswitchgearhousing" ADD CONSTRAINT "job_meterswitchgear_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e60substationgeneral" ADD CONSTRAINT "job_substation_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e60switchgear" ADD CONSTRAINT "switch_gear_e60_fk" FOREIGN KEY ("switch_gear_id") REFERENCES "core"."switchgear" ("switchgear_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e60transformer" ADD CONSTRAINT "transformer_e60_fk" FOREIGN KEY ("transformer_id_fk ") REFERENCES "core"."transformer" ("transformer_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "e84general" ADD CONSTRAINT "e84general_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "e84lineinspection" ADD CONSTRAINT "e84_general_id_fk" FOREIGN KEY ("e84_general_id") REFERENCES "core"."e84general" ("e84_general_id") ON DELETE NO ACTION ON UPDATE CASCADE;
ALTER TABLE "e84lineinspection" ADD CONSTRAINT "e84general_fk" FOREIGN KEY ("e84_general_id") REFERENCES "core"."e84general" ("e84_general_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "job" ADD CONSTRAINT "appflow_workflow_code_fk" FOREIGN KEY ("workflow_id") REFERENCES "core"."appflow" ("workflow_code") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "job" ADD CONSTRAINT "jobstatus_fk" FOREIGN KEY ("status") REFERENCES "core"."jobstatus" ("job_status_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "job" ADD CONSTRAINT "jobtype_fk" FOREIGN KEY ("type") REFERENCES "core"."jobtype" ("job_type_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "job" ADD CONSTRAINT "workOrder_work_order_id_fk" FOREIGN KEY ("work_order_id") REFERENCES "core"."workorder" ("work_order_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "jobattachment" ADD CONSTRAINT "job_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "jobprogress" ADD CONSTRAINT "jobprogress_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "core"."job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "team" ADD CONSTRAINT "team_team_leader_fkey" FOREIGN KEY ("team_leader") REFERENCES "core"."teamleader" ("team_leader") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "workorder" ADD CONSTRAINT "job_status_fk" FOREIGN KEY ("status") REFERENCES "core"."jobstatus" ("job_status_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
