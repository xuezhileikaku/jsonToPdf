<?php
$id = $_GET['id'];
$json = file_get_contents("./json/pt{$id}.json");
$arr = json_decode($json, true);


?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PT <?= $id ?></title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

    <!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">

    <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
    <style>
        p {
            font-family: Arial, Helvetica, sans-serif !important;
            overflow: visible;
            font-size: 19px;
            line-height: 1.15;
            margin-right: 12px;
            margin-top: -1.5px;
            cursor: default;
            /* border: 0px solid blue; */
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>PT<?= $id ?></h1>
        <?php foreach ($arr as $sec) { ?>
            <div class="row">
                <div class="col-sm-12">
                    <h2>Section <?= $sec['sectionOrder'] ?></h2>
                    <div class="content">
                        <h3><?= $sec['directions'] ?></h3>
                        <?php $pass = '';
                        $panum = 0;
                        $ans = [];
                        foreach ($sec['items'] as $c) {

                            if ($pass != $c['stimulusText']) {
                                $panum++;
                                $pass = $c['stimulusText'];
                                $pre = substr(trim($c["groupId"]), 0, 2);
                                if ($pre == 'RC') { ?>
                                    <h3>Passage#<?= $panum ?></h3>
                                <?php  } ?>
                                <div class="passage"><?= $pass ?></div>
                            <?php } ?>
                            <h3>Question <?= $c['itemPosition'] ?></h3>
                            <div class="title"><?= $c['stemText'] ?></div>
                            <ul style="list-style: none;padding-left: 10px;">
                                <?php foreach ($c['options'] as $i => $o) { ?>
                                    <li style="display: flex;">
                                        <div style="width: 25px;font-size: 18px;font-weight: 600;"><?= chr(65 + $i) ?>.</div>
                                        <div style=""><?= $o['optionContent'] ?></div>
                                    </li>
                                <?php } ?>
                            </ul>
                            <br />

                        <?php $ans[] = $c['correctAnswer'];
                        } ?>
                        <hr>
                    </div>
                    <div class="row">
                    <?php foreach ($ans as $l => $lv) { ?>
                                <div style="width: 323px;" class="col-4 col-sm-4">
                                    <p>Answer <?= ($l+1) .":". $lv ?></p>
                                </div>
                    <?php } ?>
                    </div>
                </div>
            </div>
        <?php } ?>
    </div>

</body>

</html>