function ceaser(text = "", key = 5) {
  let ceaserText = text.split("").map((t) => getCeaser(t, key));
  return ceaserText.join("");
}

function getCeaser(t, key = 5) {
  let charSet = "abcdedghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".split(
    ""
  );
  if (!charSet.includes(t)) return t;
  let newKey = (charSet.indexOf(t) + key) % 26;
  return charSet[newKey];
}

$("#ceaser_form").submit(function () {
	text = $("#ceaser_text").val();
	key = parseInt($("#ceaser_key").val());
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#ceaser_result").text(encryption);
});
