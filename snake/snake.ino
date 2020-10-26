int rows[8] = {2, 7, 19, 5, 13, 18, 12, 16};
int cols[8] = {6, 11, 10, 3, 17, 4, 8, 9};

int state[64] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1};

void setup() {
 Serial.begin(9600);

  Serial.println("Iniciando...");

      for (int i; i < 8; i++){
        pinMode(cols[i], OUTPUT);
        pinMode(rows[i], OUTPUT);
        digitalWrite(rows[i], LOW);
        digitalWrite(cols[i], HIGH);
      }
    }

void loop(){
  printState();

  String textoEntrada;
    // put your main code here, to run repeatedly:
    if (Serial.available()>0){
      textoEntrada = Serial.readString();
      Serial.print(" O Arduino Recebeu => ");
      Serial.println(textoEntrada);
    }
}

void printState(){
  for (int i = 0; i < 64; i += 8){
    for (int j = 0; j < 8; j++){

      if (textoEntrada[i + j] == 1){
          digitalWrite(rows[j], HIGH);
        }
      else
        digitalWrite(rows[j], LOW);
    }
    digitalWrite(cols[i / 8], LOW);
    delay(1);
    digitalWrite(cols[i / 8], HIGH);
  }
}
