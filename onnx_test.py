from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSeq2SeqLM
import time
import onnxruntime as ort
ort.set_default_logger_severity(3)


model = ORTModelForSeq2SeqLM.from_pretrained("./bart-onnx")
tokenizer = AutoTokenizer.from_pretrained("./bart-onnx")

start = time.time()
def summarize(text, model, tokenizer, max_length=1024, num_beams=4):
    inputs = tokenizer.encode("Summarize a text without adding any comment. Please summarize the following text: " + text, return_tensors="pt", max_length=max_length, truncation=True)
    summary_ids = model.generate(inputs, max_length=500, min_length=150, length_penalty=2.0, num_beams=num_beams, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

text_to_summarize = """
Russia has confirmed one of its warships has been damaged in a Ukrainian attack on a Black Sea port.
 The airstrike took place at Feodosiya in Russian-occupied Crimea early on Tuesday morning. Russia's Ministry of Defence said the large landing ship Novocherkassk was struck by Ukrainian aircraft carrying guided missiles.
 The head of the Ukrainian Air Force said earlier its warplanes had destroyed the ship. One person was killed in the attack, according to the Russian-installed head of Crimea, Sergei Aksyonov. Several others were reportedly hurt. 
 Six buildings were damaged and a small number of people had to be taken to temporary accommodation centres, Mr Aksyonov added.
 The port's transport operations are said to be functioning as normal after the area was cordoned off, while a fire caused by the attack was contained.Footage purportedly showing a huge explosion in the port was shared by Ukrainian air force commander Lt Gen Mykola Oleshchuk.The images have not been independently verified. 
 However, satellite imagery from 24 December shows a ship at port in Feodosiya that appears to be the same length as the Novocherkassk - a landing ship designed to transport troops, weapons and cargo to shore.Any significant damage to the ship will be a welcome bit of good news for Ukraine, with waning Western support now affecting its front-line operations. Given that the Novocherkassk was in dock, it is highly likely it was being loaded with soldiers, equipment or both.
 Taking it out of action, even if only temporarily, will no doubt hamper Russia's ability to supply troops in territory it occupies further north. What is less clear is how long its operations will be disrupted for and what impact this strike will have on the front lines. Meanwhile, a spokesman for Ukraine's air force has denied that Russia shot down two of its Su-24 bombers about 125km (77 miles) from the occupied Ukrainian city of Mykolaiv.
 It has also recently denied a claim by Russian Defence Minister Sergei Shoigu that his troops have seized the key town of Mariinka in eastern Ukraine.The area has been used by Ukraine as a defensive barrier since 2014, when Russian-backed fighters seized large swathes of the Donetsk and Luhansk regions.Tuesday's attack on Feodosiya is not the first time that the Novocherkassk has been targeted by Ukrainian forces.In March 2022, Ukraine's defence ministry reported that the ship had been damaged in an attack on the occupied Ukrainian port of Berdyansk in which another amphibious assault ship, the Saratov, was sunk.
 In a post on Telegram, Lt Gen Oleshchuk wrote that the Novocherkassk had gone the way of the Moskva - the flagship of Russia's Black Sea Fleet, which sank in the Black Sea last year.Ukrainian President Volodymyr Zelensky quipped that he was "grateful" to the country's air force "for the impressive replenishment of the Russian submarine Black Sea fleet with another vessel," in reference to other Russian ships that have been sunk during the war."The occupiers will not have a single peaceful place in Ukraine," he said. Russia seized and annexed the Crimean Peninsula from Ukraine in 2014 and its forces based there played a key part in the full-scale invasion of Ukraine in February 2022. Russian forces in Crimea have since come under repeated Ukrainian attack. Last month, Ukraine's military said it had destroyed 15 Russian navy ships and damaged another 12 in the Black Sea since the start of Russia's war.After a missile strike on the headquarters of the Black Sea fleet in Sevastopol last September, satellite images showed that the Russian navy had moved much of its Black Sea fleet away from Crimea to the Russian Black Sea port of Novorossiysk.The dominance of the Russian navy has been diminished to an extent as result of such attacks, but this year has seen Moscow keep hold of the territory it occupies, despite a Ukrainian counteroffensive.
"""
summary = summarize(text_to_summarize, model, tokenizer)
print(summary)

end = time.time()
print(end - start)
