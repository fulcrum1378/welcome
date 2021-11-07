from datetime import datetime, timedelta

from persiantools.jdatetime import JalaliDateTime


beg = JalaliDateTime(1400, 5, 1, 0, 0, 0).timestamp()
now = datetime.now().timestamp()
end = JalaliDateTime(1402, 2, 1, 0, 0, 0).timestamp()
title = "My Conscription Progress"
js = '''
function whenIsNow() {
    return (new Date().getTime()) / 1000;
}

var since = whenIsNow(),
    beg = parseInt(document.getElementById("beg").value),
    now = parseInt(document.getElementById("now").value),
    end = parseInt(document.getElementById("end").value),
    prog = document.getElementsByTagName("progress")[0],
    perc = document.getElementById("perc");

setInterval(function() {
    let then = now + (whenIsNow() - since),
        cA = Math.abs(end - beg),
        cB = Math.abs(then - beg),
        cC = 100.0 / cA,
        cD = cC * cB;
    perc.innerHTML = cD + "%";
    prog.value = cD;
}, 50);
'''

print("Content-type: text/html\n")
print('''<!doctype html>
<html>

<head>
  <title>''' + title + '''</title>
</head>

<body>
  <input type="hidden" value="''' + str(beg) + '''" id="beg">
  <input type="hidden" value="''' + str(now) + '''" id="now">
  <input type="hidden" value="''' + str(end) + '''" id="end">
  <center>
    <h2>''' + title + '''</h2>
    
    <progress min="0" max="100" value="0" style="width: 90%;"></progress>
    <p id="perc"></p>
  </center>
  <script type="text/javascript">''' + js + '''</script>
</body>
</html>''')
