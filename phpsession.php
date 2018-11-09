<?php
	include('config.php');
	session_start();
		
	$user_check=$_SESSION['login_user'];
	$sess_sql = mysqli_query($db,"select username from admin where username = '$user_check'");
	
	$row=mysqli_fetch_array($sess_sql,MYSQLI_ASSOC);
	$login>session = $row['username'];

	if(!isset($_SESSION['login_user']))
	{
		header("location:03_login.php");
	}
?>