void hist1d_2(std::string filename, std::string _title="", int nbins=300, double xmin=50., double xmax=350.)
{
    #include <fstream>

    ifstream ifs(filename);

    TString title = _title; // TString型に変換しないとエラーが出る

    TH1F * h1 = new TH1F("ADC", title, nbins, xmin, xmax);

    //データをヒストグラムに詰める
    double x;
    while(ifs>>x) h1->Fill(x);
    ifs.close();

    //ヒストグラムの描画
    // h1->SetLineColor(kBlue);
    // h1->SetLineWidth(2);
    h1->SetStats(0);
    h1->GetXaxis()->SetTitle("ADC");
    h1->GetYaxis()->SetTitle("Counts");
    h1->Draw(); //ヒストグラムを描く
}