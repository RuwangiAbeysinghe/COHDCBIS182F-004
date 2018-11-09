<?php
	include("config.php");
	session_start();
	if($_SERVER["REQUEST_METHOD"]=="POST")
	{
		$uname=mysqli_real_escape_string($db,$_POST['username']);
		$pwd=mysqli_real_escape_string($db,$_POST['password']);
		
		$sql = "select id from admini where username = '$uname' and password = '$pwd'";
		$output = mysql_query($db,$sql);
		$row=mysqli_fetch_array($output,MYSQLI_ASSOC);
		$active = $row['active'];

		$count=mysql_num_rows($output);
		
		if($count==1)
		{
			session_register("uname");
			$_SESSION['login_user']=$uname;
			header("location: home.php");
		}
		else
		{
			$error="Login name or Password is invalid";
		}
	}
?>