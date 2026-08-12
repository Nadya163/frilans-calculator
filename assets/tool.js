(function () {
  "use strict";

  var CFG = window.CALC_CONFIG || {};
  var mainMode    = CFG.mainMode   !== undefined ? CFG.mainMode   : "net";
  var showHourly  = CFG.showHourly !== undefined ? CFG.showHourly : true;
  var showLimit   = CFG.showLimit  !== undefined ? CFG.showLimit  : false;

  var RATE         = { fl: 0.04, ul: 0.06 };
  var REDUCED_RATE = { fl: 0.03, ul: 0.04 };

  function round2(n) { return Math.round(n * 100) / 100; }

  function fmt(n) {
    if (isNaN(n) || !isFinite(n)) return "—";
    return round2(n).toLocaleString("ru-RU", {
      minimumFractionDigits: 0,
      maximumFractionDigits: 2,
    }) + " ₽";
  }

  function taxFromGross(gross, type, ded) {
    var rate    = RATE[type];
    var reduced = REDUCED_RATE[type];
    var stdTax  = gross * rate;
    if (!ded || ded <= 0) return { tax: stdTax, deductionUsed: 0 };
    var saving = Math.min(gross * (rate - reduced), ded);
    return { tax: stdTax - saving, deductionUsed: saving };
  }

  function grossFromNet(net, type, ded) {
    var rate    = RATE[type];
    var reduced = REDUCED_RATE[type];
    var D = ded || 0;
    if (D <= 0) return net / (1 - rate);
    var grossA = net / (1 - reduced);
    if (grossA <= D / (rate - reduced)) return grossA;
    return (net - D) / (1 - rate);
  }

  function initMainCalc() {
    var wrap = document.getElementById("calc-main");
    if (!wrap) return;

    if (mainMode === "hidden") {
      wrap.style.display = "none";
      var sep = document.getElementById("hourly-sep");
      if (sep) sep.style.display = "none";
      return;
    }

    var mode          = mainMode;
    var modeNetBtn    = document.getElementById("modeNet");
    var modeGrossBtn  = document.getElementById("modeGross");
    var amountInput   = document.getElementById("amount");
    var amountLabel   = document.getElementById("amountLabel");
    var clientType    = document.getElementById("clientType");
    var useDeduction  = document.getElementById("useDeduction");
    var deductionRow  = document.getElementById("deductionRow");
    var dedInput      = document.getElementById("deductionRemaining");

    var resMainLabel  = document.getElementById("resultMainLabel");
    var resMain       = document.getElementById("resultMain");
    var resTax        = document.getElementById("resultTax");
    var resRate       = document.getElementById("resultRate");
    var resDedRow     = document.getElementById("resultDeductionRow");
    var resDedLeft    = document.getElementById("resultDeductionLeft");

    function setMode(m) {
      mode = m;
      modeNetBtn.classList.toggle("active",   mode === "net");
      modeGrossBtn.classList.toggle("active", mode === "gross");
      amountLabel.textContent   = mode === "net"
        ? "Сумма от клиента, ₽"
        : "Сколько хотите получить на руки, ₽";
      resMainLabel.textContent  = mode === "net"
        ? "Получите на руки"
        : "Выставите клиенту";
      calc();
    }

    function calc() {
      var amount  = parseFloat(amountInput.value) || 0;
      var type    = clientType.value;
      var dedOn   = useDeduction.checked;
      var ded     = dedOn ? (parseFloat(dedInput.value) || 0) : 0;

      var gross, tax, deductionUsed;

      if (mode === "net") {
        gross = amount;
        var r = taxFromGross(gross, type, ded);
        tax   = r.tax; deductionUsed = r.deductionUsed;
        resMain.textContent = fmt(gross - tax);
      } else {
        var net = amount;
        gross   = grossFromNet(net, type, ded);
        var r2  = taxFromGross(gross, type, ded);
        tax     = r2.tax; deductionUsed = r2.deductionUsed;
        resMain.textContent = fmt(gross);
      }

      resTax.textContent  = "−" + fmt(tax);
      resRate.textContent = type === "fl" ? "физлицо 4%" : "юрлицо / ИП 6%";

      if (dedOn) {
        resDedRow.style.display = "flex";
        resDedLeft.textContent  = fmt(Math.max(ded - deductionUsed, 0));
      } else {
        resDedRow.style.display = "none";
      }
      updateLimit(gross);
    }

    modeNetBtn.addEventListener("click",   function () { setMode("net"); });
    modeGrossBtn.addEventListener("click", function () { setMode("gross"); });
    amountInput.addEventListener("input",  calc);
    clientType.addEventListener("change",  calc);
    useDeduction.addEventListener("change", function () {
      deductionRow.style.display = useDeduction.checked ? "flex" : "none";
      calc();
    });
    dedInput.addEventListener("input", calc);

    setMode(mode);
  }

  function initHourlyCalc() {
    var wrap = document.getElementById("calc-hourly");
    if (!wrap) return;

    if (!showHourly) {
      wrap.style.display = "none";
      var title = document.getElementById("hourly-title");
      var sub   = document.getElementById("hourly-sub");
      if (title) title.style.display = "none";
      if (sub)   sub.style.display   = "none";
      return;
    }

    var rateInput  = document.getElementById("hourlyRate");
    var hoursInput = document.getElementById("hoursPerWeek");
    var weeksInput = document.getElementById("weeksPerMonth");
    var typeSelect = document.getElementById("clientTypeHourly");
    var dedCb      = document.getElementById("useDeductionHourly");
    var dedRow     = document.getElementById("deductionRowHourly");
    var dedInput   = document.getElementById("deductionRemainingHourly");

    var elGross    = document.getElementById("hourlyGross");
    var elTax      = document.getElementById("hourlyTax");
    var elNet      = document.getElementById("hourlyNet");
    var elDay      = document.getElementById("hourlyDay");  

    function calc() {
      var rate   = parseFloat(rateInput.value)  || 0;
      var hours  = parseFloat(hoursInput.value) || 0;
      var weeks  = parseFloat(weeksInput.value) || 0;
      var type   = typeSelect.value;
      var dedOn  = dedCb.checked;
      var ded    = dedOn ? (parseFloat(dedInput.value) || 0) : 0;

      var gross  = rate * hours * weeks;
      var r      = taxFromGross(gross, type, ded);
      var net    = gross - r.tax;
      var hoursPerDay = 8; 

      elGross.textContent = fmt(gross);
      elTax.textContent   = "−" + fmt(r.tax);
      elNet.textContent   = fmt(net);
      if (elDay) elDay.textContent = fmt(rate * hoursPerDay * (1 - RATE[type]));

      updateLimit(gross);
    }

    [rateInput, hoursInput, weeksInput, dedInput].forEach(function (el) {
      el.addEventListener("input", calc);
    });
    typeSelect.addEventListener("change", calc);
    dedCb.addEventListener("change", function () {
      dedRow.style.display = dedCb.checked ? "flex" : "none";
      calc();
    });

    calc();
  }

  function initLimitBlock() {
    var wrap = document.getElementById("limit-block");
    if (!wrap) return;
    wrap.style.display = showLimit ? "block" : "none";
  }

  function updateLimit(monthlyGross) {
    var bar   = document.getElementById("limitBar");
    var label = document.getElementById("limitLabel");
    if (!bar || !label || !showLimit) return;

    var LIMIT  = 2400000;
    var months = 12;
    var annual = monthlyGross * months;
    var pct    = Math.min(annual / LIMIT * 100, 100);

    bar.style.width = pct.toFixed(1) + "%";
    bar.style.background = pct >= 90 ? "#ff7a7a" : pct >= 70 ? "#f2b705" : "#35d99c";

    var left = Math.max(LIMIT - annual, 0);
    label.textContent = pct >= 100
      ? "⚠️ Годовой лимит 2 400 000 ₽ превышен — нужно менять режим!"
      : "Прогноз за год: " + fmt(annual) + " из 2 400 000 ₽ · Остаток: " + fmt(left);
  }

  document.addEventListener("DOMContentLoaded", function () {
    initLimitBlock();
    initMainCalc();
    initHourlyCalc();
  });

})();
