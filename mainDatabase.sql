drop database pmt;
create database pmt;
use pmt;
show tables;



CREATE TABLE Project_Details (
  Project_ID INT PRIMARY KEY auto_increment,
  Project_Name VARCHAR(20) NOT NULL,
  Project_Description VARCHAR(100) NOT NULL,
  Planned_SD datetime NOT NULL,
  Planned_ED datetime NOT NULL,
  Actual_SD DATETIME NOT NULL,
  Actual_ED DATETIME NOT NULL,
  Planned_Hours varchar(30) not null,
  Actual_Hours varchar(30) not null,
  Status ENUM('To_do','In_Progress', 'In_Review', 'Done') DEFAULT "To_do",
  Project_Lead VARCHAR(20),
  Client_Name VARCHAR(20),
  Risk VARCHAR(50),
  Mitigation VARCHAR(100)
);

ALTER TABLE Project_Details AUTO_INCREMENT=100;

insert into Project_Details(project_name,project_description,planned_sd,planned_ed,
actual_sd,actual_ed,planned_hours,actual_hours,status,project_lead,client_name,risk,mitigation) values
("trial","trial2",now(),now(),now(),now(),"30 minute","40 minute","To_do","pratik","tcs","high","no");

desc Project_details;

select * from Project_details;



CREATE TABLE Users (
  user_ID INT PRIMARY KEY auto_increment,
  roles varchar(50) Not Null,
  Name VARCHAR(30) NOT NULL,
  Email_ID VARCHAR(30) UNIQUE NOT NULL,
  Password VARCHAR(100) NOT NULL,
  Contact decimal(10) NOT NULL
);

ALTER TABLE Users AUTO_INCREMENT=2000;

insert into Users(roles,name,email_id,password,contact)values("project Manager","rupa","rupa@gmail.com","123",8598);
select * from Users;

create table project_member(member_id int primary key auto_increment,
user_ID int not null,
Project_ID int not null;


ALTER TABLE project_member AUTO_INCREMENT=1;

insert into project_member(user_id,project_id) values(2000,100);

select * FROM project_member;


CREATE TABLE Issue_Details (
  Issue_Id INT PRIMARY KEY auto_increment,
  Issue_name varchar(30),
  Description VARCHAR(100)
);

ALTER TABLE Issue_Details AUTO_INCREMENT=3000;

insert into Issue_Details(Issue_name,Description) values("issue1","no desc");

select * from Issue_Details;


CREATE TABLE Task (
  Task_ID INT PRIMARY KEY auto_increment ,
  Issue_ID INT NOT NULL,
  Description VARCHAR(100) NOT NULL,
  Status ENUM('To_do', 'In_Progress', 'In_Review', 'Done') default null ,
  task_SD DATE NOT NULL,
  task_ED DATE NOT NULL,
  Planned_Hours varchar(30) not null,
  Actual_Hours varchar(30) not null,
  Priority varchar(50),
  FOREIGN KEY (Issue_ID) REFERENCES Issue_Details(Issue_Id)
  );
  
  Alter table Task auto_increment=5000;
  
  insert into Task(Task_ID,Issue_ID,Description,task_SD,task_ED,Planned_Hours,Actual_Hours,Priority) 
  values(5000,3000,"desc",CURDATE(),CURDATE(),"no","no","high");
  
  select * from Task;


CREATE TABLE defect(
  defect_ID INT PRIMARY KEY auto_increment,
  Issue_ID INT NOT NULL,
  Description VARCHAR(100),
  Status  ENUM('To_do', 'In_Progress', 'In_Review', 'Done') default null,
  defect_SD DATE NOT NULL,
  defect_ED DATE NOT NULL,
  Planned_Hours varchar(30) not null,
  Actual_Hours varchar(30) not null,
  FOREIGN KEY (Issue_ID) REFERENCES Issue_Details(Issue_Id)
  );
  
alter table defect auto_increment=7000;
#insert into defect(defect_ID,Issue_ID,Description,task_SD,task_ED,Planned_Hours,Actual_Hours,Priority); 
#values('1001',100,"desc",CURDATE(),CURDATE(),"no","no","high"); 
  
create table issue_member(issueMember_id int primary key auto_increment,
issue_ID int not null,
user_ID int not null,
project_ID int not null;



ALTER TABLE issue_member AUTO_INCREMENT=1;

insert into issue_member(issue_ID,user_ID,project_ID) values(3000,2000,100);
select * from issue_member;


  
create table file(file_id int auto_increment primary key,
file_link varchar(100),
issue_id int not null,
foreign key(issue_id) references Issue_Details(issue_id));



create table Issueworkflow_Connection(sr_no int primary key auto_increment,
issue_id int not null unique,
workflow_name varchar(50) not null,
foreign key(issue_id) references Issue_Details(issue_id));

create table Projectworkflow_Connection(sr_no int primary key auto_increment,
project_id int not null,
workflow_name varchar(50) not null,
foreign key(project_id) references Project_Details(project_id));

CREATE TABLE alpha_user (user_name VARCHAR(20) not null,Password VARCHAR(100) NOT NULL);

insert into alpha_user values("infobellIT","infobell@123");

CREATE TABLE comments (comment_ID INT auto_increment PRIMARY KEY,ID INT NOT NULL,description VARCHAR(100) NOT NULL,date date NOT NULL);

CREATE TABLE workflow (
  workflow_name VARCHAR(20) NULL DEFAULT NULL,
  prev_state VARCHAR(20) NULL DEFAULT NULL,
  current_state VARCHAR(20) NULL DEFAULT NULL,
  next_state VARCHAR(20) NULL DEFAULT NULL);





