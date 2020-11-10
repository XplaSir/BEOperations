/*
 Navicat Premium Data Transfer

 Source Server         : beops
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 26/08/2019 14:18:20
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for appflow
-- ----------------------------
DROP TABLE IF EXISTS "appflow";
CREATE TABLE "appflow" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "appflow_id" character varying(100) NOT NULL,
  "section" character varying(100),
  "app" character varying(50),
  "workflow_code" character varying(100),
  CONSTRAINT "appflow_pkey" PRIMARY KEY ("appflow_id"),
  CONSTRAINT "appflow_workflow_code_uc" UNIQUE ("workflow_code" ASC)
);

-- ----------------------------
-- Table structure for centre
-- ----------------------------
DROP TABLE IF EXISTS "centre";
CREATE TABLE "centre" (
  "centre_id" character varying(100) NOT NULL,
  "centre_code" character varying(100),
  "centre_name" character varying(100),
  "cost_centre" character varying(100),
  "type" character varying(100),
  CONSTRAINT "centre_pkey" PRIMARY KEY ("centre_id")
);

-- ----------------------------
-- Table structure for e84general
-- ----------------------------
DROP TABLE IF EXISTS "e84general";
CREATE TABLE "e84general" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "e84_general_id" character varying(100) NOT NULL,
  "job_id" character varying(100),
  "district" character varying(100),
  "line_section" character varying(100),
  "section_number" character varying(100),
  "construction_type" character varying(100),
  "comment" text,
  "overall_result" character varying(100),
  CONSTRAINT "e84_general_id_pk" PRIMARY KEY ("e84_general_id"),
  CONSTRAINT "e84general_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for e84lineinspection
-- ----------------------------
DROP TABLE IF EXISTS "e84lineinspection";
CREATE TABLE "e84lineinspection" (
  "line_inspection_id" character varying(100) NOT NULL,
  "job_id" character varying(100),
  "pole_number" character varying(100),
  "pole_type" character varying(100),
  "wayleave" character varying(100),
  "comment" character varying(100),
  "cross_arm" character varying(100),
  "insulator" character varying(100),
  "conductors" character varying(100),
  "stays" character varying(100),
  "earthing" character varying(100),
  "cradles" character varying(100),
  "anti_climbing_device" character varying(100),
  "created_by" character varying(100),
  "created_on" timestamp without time zone,
  "modified_by" character varying(100),
  "modified_on" timestamp without time zone,
  CONSTRAINT "line_inspection_id_pk" PRIMARY KEY ("line_inspection_id"),
  CONSTRAINT "e84lineinspection_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "job" ("job_id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------------
-- Table structure for feeder
-- ----------------------------
DROP TABLE IF EXISTS "feeder";
CREATE TABLE "feeder" (
  "feeder_id_pk" character varying(100) NOT NULL,
  "name" character varying(100),
  "equipment_id" character varying(100),
  "voltage" character varying(100),
  "feeder_number" character varying(100),
  "centre" character varying(100),
  CONSTRAINT "feeder_id_pkey" PRIMARY KEY ("feeder_id_pk")
);

-- ----------------------------
-- Table structure for job
-- ----------------------------
DROP TABLE IF EXISTS "job";
CREATE TABLE "job" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "job_id" character varying(100) NOT NULL,
  "work_order_id" character varying(100),
  "type" character varying(100),
  "description" text,
  "asset_id" character varying(100),
  "assignee" character varying(100),
  "comments" text,
  "closed_by" character varying(100),
  "closed_dt" timestamp without time zone,
  "asset_name" character varying(100),
  "asset_type" character varying(100),
  "asset_number" character varying(100),
  "expected_end_dt" timestamp without time zone,
  "reference_no" character varying(100),
  "asset_serial" character varying(100),
  "geom" geography,
  "workflow_id" character varying(100),
  CONSTRAINT "job_job_id_pk" PRIMARY KEY ("job_id"),
  CONSTRAINT "workOrder_work_order_id_fk" FOREIGN KEY ("work_order_id") REFERENCES "workorder" ("work_order_id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------------
-- Table structure for job_status
-- ----------------------------
DROP TABLE IF EXISTS "job_status";
CREATE TABLE "job_status" (
  "job_status_id" character varying(100) NOT NULL,
  "status" character varying(100),
  CONSTRAINT "job_status_pkey" PRIMARY KEY ("job_status_id")
);

-- ----------------------------
-- Table structure for job_type
-- ----------------------------
DROP TABLE IF EXISTS "job_type";
CREATE TABLE "job_type" (
  "job_type_id" character varying(100) NOT NULL,
  "type" character varying(100),
  CONSTRAINT "job_type_pkey" PRIMARY KEY ("job_type_id")
);

-- ----------------------------
-- Table structure for jobattachment
-- ----------------------------
DROP TABLE IF EXISTS "jobattachment";
CREATE TABLE "jobattachment" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "job_attach_id" character varying(100) NOT NULL,
  "job_id" character varying(100),
  "comments" character varying(100),
  "attachment" bytea,
  CONSTRAINT "jobAttachment_pkey" PRIMARY KEY ("job_attach_id"),
  CONSTRAINT "job_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for jobprogress
-- ----------------------------
DROP TABLE IF EXISTS "jobprogress";
CREATE TABLE "jobprogress" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "job_progress_id" character varying(100) NOT NULL,
  "job_id" character varying(100),
  "start_dt" timestamp without time zone,
  "end_dt" timestamp without time zone,
  "fleet_no" character varying(100),
  "open_mileage" integer,
  "close_mileage" integer,
  "geom_start" geometry,
  "geom_end" geometry,
  "comments" text,
  "action" character varying(100),
  "status" character varying(100),
  CONSTRAINT "job_progress_pkey" PRIMARY KEY ("job_progress_id"),
  CONSTRAINT "jobprogress_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for jobteam
-- ----------------------------
DROP TABLE IF EXISTS "jobteam";
CREATE TABLE "jobteam" (
  "job_team_id" character varying(100) NOT NULL,
  "job_progress_id" character varying(100),
  "ec_num" character varying(100),
  "start_dt" character varying(100),
  "end_dt" character varying(100),
  "teamleader" character varying(100),
  "created_by" character varying(100),
  "created_on" timestamp without time zone,
  "modified_by" character varying(100),
  "modified_on" timestamp without time zone,
  CONSTRAINT "jobTeam_pkey" PRIMARY KEY ("job_team_id")
);

-- ----------------------------
-- Table structure for jobworkflow
-- ----------------------------
DROP TABLE IF EXISTS "jobworkflow";
CREATE TABLE "jobworkflow" (
  "job_workflow_id" character varying(100) NOT NULL,
  "ec_num" character varying(100),
  "action" character varying(100),
  "job_id" character varying(100),
  "action_dt" character varying(100),
  "workflow_id" character varying(100),
  "created_by" character varying(100),
  "created_on" timestamp without time zone,
  "modified_by" character varying(100),
  "modified_on" timestamp without time zone,
  CONSTRAINT "jobWorkFlow_jobWorkFlow_id_pk" PRIMARY KEY ("job_workflow_id"),
  CONSTRAINT "job_job_id_fk" FOREIGN KEY ("job_id") REFERENCES "job" ("job_id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for office
-- ----------------------------
DROP TABLE IF EXISTS "office";
CREATE TABLE "office" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "office_id" character varying(100) NOT NULL,
  "supervisor_id" character varying(100),
  "office_description" character varying(100),
  CONSTRAINT "office_pkey" PRIMARY KEY ("office_id")
);

-- ----------------------------
-- Table structure for pole
-- ----------------------------
DROP TABLE IF EXISTS "pole";
CREATE TABLE "pole" (
  "pole_id" character varying(100) NOT NULL,
  "equipment_id" character varying(100),
  "pole_no" character varying(100),
  "pole_type" character varying(100),
  "centre" character varying(100),
  CONSTRAINT "pole_id_pkey" PRIMARY KEY ("pole_id")
);

-- ----------------------------
-- Table structure for team
-- ----------------------------
DROP TABLE IF EXISTS "team";
CREATE TABLE "team" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "team_id" character varying(100) NOT NULL,
  "team_leader" character varying(100),
  "team_member" character varying(100),
  "specialisation" character varying(100),
  CONSTRAINT "team_team_id_pk" PRIMARY KEY ("team_id")
);

-- ----------------------------
-- Table structure for teamleader
-- ----------------------------
DROP TABLE IF EXISTS "teamleader";
CREATE TABLE "teamleader" (
  "team_leader" character varying(100) NOT NULL,
  "specialisation" character varying(100),
  CONSTRAINT "teamleader_pkey" PRIMARY KEY ("team_leader")
);

-- ----------------------------
-- Table structure for workflow
-- ----------------------------
DROP TABLE IF EXISTS "workflow";
CREATE TABLE "workflow" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "workflow_id" character varying(100) NOT NULL,
  "workflow_code" character varying(100),
  "office_id" character varying(100),
  "step" integer,
  "approve" character varying(100),
  "reject" character varying(100),
  CONSTRAINT "workflow_pkey" PRIMARY KEY ("workflow_id"),
  CONSTRAINT "appflow_workflow_code_fk" FOREIGN KEY ("workflow_code") REFERENCES "appflow" ("workflow_code") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "office_office_id_fk" FOREIGN KEY ("office_id") REFERENCES "office" ("office_id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for workorder
-- ----------------------------
DROP TABLE IF EXISTS "workorder";
CREATE TABLE "workorder" (
  "created_by" character varying,
  "created_on" timestamp without time zone,
  "modified_by" character varying,
  "modified_on" timestamp without time zone,
  "work_order_id" character varying(100) NOT NULL,
  "description" character varying(100),
  "centre" character varying(100),
  "comments" character varying(100),
  "status" character varying(100),
  CONSTRAINT "workOrder_work_order_id_pk" PRIMARY KEY ("work_order_id")
);

PRAGMA foreign_keys = true;
