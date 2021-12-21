/*
const $ = require("jquery");
const ceaser = require("./ceaser.js");
const playfair = require("playfair");
*/

/*   		Cesear 	   */

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

/*   		Play Fair 	 */
$("#pf_enc_btn").click(function () {
	text = $("#pf_text").val();
	console.log(text)
	key = parseInt($("#pf_key").val());
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#pf_enctxt").val(encryption);
});

$("#pf_denc_btn").click(function () {
	text = $("#pf_enctxt").val();
	key = parseInt($("#pf_key").val());
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#pf_text").val(encryption);
});

/*       AutoKey     */
$("#ak_enc_btn").click(function () {
	text = $("#autokey_text").val();
	key = parseInt($("#ak_key").val());
	console.log(text,key);
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#ak_enctxt").val(encryption);
});

$("#ak_denc_btn").click(function () {
	text = $("#ak_enctxt").val();
	key = parseInt($("#ak_key").val());
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#autokey_text").val(encryption);
});

/*  		Vigenere 		*/
$("#vg_enc_btn").click(function () {
	text = $("#vg_text").val();
	key = parseInt($("#vg_key").val());
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#vg_enctxt").val(encryption);
});

$("#vg_denc_btn").click(function () {
	text = $("#vg_enctxt").val();
	key = parseInt($("#vg_key").val());
	encryption = ceaser(text, key);
	console.log(encryption);
	$("#vg_text").val(encryption);
});
