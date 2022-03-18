<svelte:head>
	<title>Work</title>
	<link rel="stylesheet" href="src/css/styleForWork.css">
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400&display=swap" rel="stylesheet">
</svelte:head>

<section>
	<div class="container">
		<header>
			<div class="content">
				<img class="logo" src="/static/logo.png" alt="">
				<h1 class="header-title">CPP Segmentation<br>error</h1>	
				<div class="nav">
					<!-- svelte-ignore a11y-invalid-attribute -->
					<a href="">Team</a>
					<!-- svelte-ignore a11y-invalid-attribute -->
					<a href="">Home Page</a>
				</div>
			</div>
			<hr>
		</header>
	</div>
</section>
<section>
    <div class="conteiner">
        <div class="titles-content">
            <h1 class="title">Попробуйте наш сервис по прогнозированию цены  товара </h1>
        </div>
        <div class="main-content">
            <div class="left-menu">
                <!-- svelte-ignore a11y-invalid-attribute -->
                <a class="btn" href="">Введите ссылку на файл</a>
                <h1 class="menu-title">Как это работает?</h1>
                <p class="menu-description">Программа представляет собой<br>веб приложение, основной скрипт<br>которого написан на Python.<br>Скрипт работает по следующему<br>принципу: Загружается база<br>данных, скрипт получает значения<br>из базы и обрабатывает их<br>согласно написанной<br>математической модели </p>
            </div>
            <div class="right-menu">
                <!-- svelte-ignore a11y-invalid-attribute -->
                <a class="btn" href="">Выберите наименование</a>
                <h1 class="menu-title">Почему это полезно?</h1>
                <p class="menu-description">Данный сервис по сути своей<br>является огромным бонусом для<br>предприятий, которые ведут<br>закупки в больших объемах. Это<br>позволит более эффективно вести<br>бухгалтерию и также снизит<br>расходы компании</p>
            </div>
        </div>
    </div>
</section>
<section>
    {#if !ready}
    <div class="stat-menu">
        <div class="stat-bar"></div>
        <h1 class="stat-bar-title">76% completed</h1>
    </div>
    {/if }
        
    <div class="result">
        <div class="result-menu">
            <h1 class="result-title">В ближайшее время,<br>на основе загруженной базы<br>данных, выбранный вами<br>товар будет стоит <strong>[price]$</strong></h1>
        </div>
    </div>
</section>
<script>
    let ready = true;
</script>