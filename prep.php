<?php
$id = $_GET['id'];
$json = file_get_contents("./json/pt{$id}.json");
$arr = json_decode($json, true);


?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Question Display</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css"
          integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

    <!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap-theme.min.css"
          integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">

    <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js"
            integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous">
    </script>

    <style>
        .question-container {
            /*margin: 20px;*/
            padding: 20px;
            /*border: 1px solid #ccc;*/
        }

        p {
            font-size: 20px;
        }

        .ops-ul {
            list-style: none;
            /*display: flex;*/
        }

        .ops-label {
            width: 26px;
            font-size: 19px;
            font-weight: 600;
        }

        /*.ops-val > p {*/
        /*    margin-left: 25px;*/
        /*    margin-top: -27px;*/
        /*}*/
    </style>
</head>

<body>

<div class="container">
    <h1>PT<?= $id ?></h1>
    <?php foreach ($arr as $sec) { ?>
        <h2>Section <?= $sec['sectionOrder'] ?></h2>
        <p><?= $sec['directions'] ?></p>
        <br>
        <div class="row">
            <div class="ques-con">
                <div>
                    <?php $pass = '';
                    $ans = [];
                    $panum = 0;
                    foreach ($sec['items'] as $q) {
                        $pre = substr(trim($q['groupId']), 0, 2);
                        if ($pre == 'RC') {
                            if ($pass !== $q['stimulusText']) {
                                $panum++;
                                $pass = $q['stimulusText']; ?>
                                <h3>Passage#<?= $panum ?></h3>
                                <div><?= $pass ?></div>
                            <?php } ?>
                        <?php } else { ?>
                            <div><?= $q['stimulusText'] ?></div>
                        <?php } ?>
                        <h3>Question <?= $q['itemPosition'] ?></h3>
                        <div><?= $q['stemText'] ?></div>
                        <div class="ops-ul">
                            <?php foreach ($q['options'] as $op) { ?>
                                <div class="row">
                                    <div class="ops-val"><?= str_replace('<p>','<p>'. $op['optionLetter'].'. ',$op['optionContent']) ?>
                                    </div>
                                </div>
                            <?php } ?>
                        </div>
                        <br>
                        <?php $ans[] = $q['correctAnswer'];
                    } ?>
                </div>
            </div>
            <hr>
            <div class="row">
                <?php foreach ($ans as $j => $a) { ?>
                    <div class="col-4 col-sm-4" style="font-size: 19px;">Answer <?= $j + 1 ?>:<?= $a ?></div>
                <?php } ?>

            </div>
        </div>
        <hr>
    <?php } ?>
</div>
<script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"
        integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ" crossorigin="anonymous">
</script>
<!-- Bootstrap JS and jQuery -->
<script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js"></script>
</body>

</html>