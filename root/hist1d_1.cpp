{
    #include <fstream>

    ifstream ifs("../data/MPPC_data/S14_412.dat"); //ヒストグラムを作りたいファイル名を入れる

    TH1F * h1 = new TH1F("ADC", "", 300, 50., 350.); // label, title, nbins, xmin, xmax

    // データをヒストグラムに詰める
    double x;
    while(ifs>>x) h1->Fill(x);
    ifs.close();

    h1->Draw(); //ヒストグラムを描く
}