create database pmt;
use pmt;
CREATE TABLE Project_Details (
  Project_ID INT PRIMARY KEY auto_increment,
  Project_Name VARCHAR(20) NOT NULL,
  Project_Description VARCHAR(100) NOT NULL,
  Planned_SD date NOT NULL,
  Planned_ED date NOT NULL,
  Actual_SD DATE NOT NULL,
  Actual_ED DATE NOT NULL,
  Planned_Hours varchar(30) not null,
  Actual_Hours varchar(30) not null,
  Status ENUM('To_do','In_Progress', 'In_Review', 'Done') DEFAULT "To_do",
  Project_Lead VARCHAR(20),
  Client_Name VARCHAR(20),
  Risk VARCHAR(50),
  Mitigation VARCHAR(100)
);

INSERT INTO Project_Details (Project_Name, Project_Description, Planned_SD, Planned_ED, Actual_SD, Actual_ED, Planned_Hours, Actual_Hours, Project_Lead, Client_Name, Risk, Mitigation)
VALUES ('Project A', 'Description of Project A', '2023-07-01', '2023-09-30', '2023-07-05', '2023-09-25', '200 hours', '180 hours', 'John Doe', 'Client X', 'Technical challenges', 'Collaboration with experienced developers');


ALTER TABLE Project_Details AUTO_INCREMENT=100;
select * from Project_Details;

CREATE TABLE Users (
  user_ID INT PRIMARY KEY auto_increment,
  roles varchar(50) Not Null,
  Name VARCHAR(30) NOT NULL,
  Email_ID VARCHAR(30) UNIQUE NOT NULL,
  Password VARCHAR(100) NOT NULL,
  Contact decimal(10) NOT NULL
);

ALTER TABLE Users AUTO_INCREMENT=2000;


select * from Users;

-------------------------------------------------------

create table project_member (member_id int primary key auto_increment, user_ID int not null, project_ID int not null);


ALTER TABLE project_member AUTO_INCREMENT=1;


select * FROM project_member;

--------------------------------------------------------

CREATE TABLE Issue_Details (
  issue_id INT PRIMARY KEY auto_increment,
  issue_name varchar(30),
  description VARCHAR(100),
  type ENUM('task','defect'),
  status VARCHAR(30)
);

ALTER TABLE Issue_Details AUTO_INCREMENT=3000;


select * from Issue_Details;
desc Issue_Details;

--------------------------------------------------------

CREATE TABLE Task (
  task_id INT PRIMARY KEY auto_increment ,
  issue_id INT NOT NULL,
  title VARCHAR(30) NOT NULL,
  task_sd DATE NOT NULL,
  task_ed DATE NOT NULL,
  estimated_time varchar(30) not null,
  priority ENUM('High', 'Medium', 'Low'),
  file_attachment TEXT DEFAULT NULL,
  FOREIGN KEY (issue_id) REFERENCES Issue_Details(issue_id)
  );
 
 
  Alter table Task auto_increment=5000;
  
  select * from Task;
-------------------------------------------------------

CREATE TABLE Defect(
  defect_id INT PRIMARY KEY auto_increment,
  issue_id INT NOT NULL,
  title VARCHAR(30) NOT NULL,
  product VARCHAR(50) NOT NULL,
  component TEXT NOT NULL,
  component_description TEXT default null,
  version VARCHAR(20),
  severity ENUM('Critical','Major','Minor'),
  OS ENUM('Windows','Mac','Linux'),
  summary TEXT NOT NULL,
  defect_sd DATE NOT NULL,
  defect_ed DATE NOT NULL,
  priority ENUM('High', 'Medium', 'Low'),
  estimated_time varchar(30) not null,
  file_attachment TEXT DEFAULT NULL,
  FOREIGN KEY (issue_id) REFERENCES Issue_Details(issue_id)
  );
  
alter table Defect auto_increment=7000;

select * from Defect;
desc Defect;
--------------------------------------------------------
  
create table Issue_Member(issueMember_id int primary key auto_increment,
issue_id int not null,
user_id int not null,
project_id int not null);


ALTER TABLE Issue_Member AUTO_INCREMENT=1;

--------------------------------------------------------
CREATE TABLE comments (comment_ID INT auto_increment PRIMARY KEY,ID INT NOT NULL,description VARCHAR(100) NOT NULL,user_id int not null,author_name varchar(50) not null,date date NOT NULL,foreign key(user_id) references users(user_id));
create table workflow (workflow_name varchar(30),workflow text);
create table workflowconnection (project_id int,workflow_name varchar(30),issue_type enum('task,defect'));

show tables;

desc defect;