from ROOT import TCanvas, TH1F

def quit():
    temp = input('quit? [y/n] >> ')
    if temp == 'y':
        print('quit')
    else:
        return quit()

if __name__=="__main__":
    c = TCanvas("c", "", 800, 600) # キャンバスの作成
    h1 = TH1F("Edep","Energy deposit in Absorbers", 100, 0., 1000.) # ヒストグラムの作成

    with open("../data/output.dat", "r") as f:
        data = f.read().split("\n") # データをリスト型で読み込む

    for d in data:
        h1.Fill(float(d)) #ヒストグラムのFill

    h1.Draw()
    c.Update()

    quit() # これがないとGUIがすぐ閉じてしまう

    # キャンバスの保存
    isSave = input("Save Canvas? [y/n] >>")
    if isSave == "y":
        c.SaveAs("images/output.png")
        c.SaveAs("images/output.pdf")
    else:
        pass