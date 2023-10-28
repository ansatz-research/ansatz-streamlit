import streamlit as st
import pandas as pd
import os
from glob import glob
import numpy as np
pd.options.plotting.backend = "plotly"

def adjust_by_precision(x):

    # try:
        # st.write(x['outAmount'])
        # print(x['outAmount'])
        oA = float(x.loc['outAmount'])
        if x.loc['outputMint'] == 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v':
            oA /= 1e6
        else:
            oA /= 1e9
        iA = float(x.loc['inAmount']) 
        if x.loc['inputMint'] == 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v':
            iA /= 1e6
        else:
            iA /= 1e9
        return (oA, iA)
    # except:
    #     return (np.nan, np.nan)

def main():
    # URL of the image
    image_url = "https://pbs.twimg.com/profile_images/1716188114652168192/pBfDyMkG_400x400.jpg"

    # Display the image centered using Markdown and HTML
    st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{image_url}" alt="Image" style="width: 400px; height: 400px;"></div>', unsafe_allow_html=True)
    # Add CSS animation for changing font color
    st.markdown('''
    <style>
        @keyframes changeColor {
             0% { color: #0072b1; }
            20% { color: #1E90FF; } /* DodgerBlue */
            40% { color: #9932CC; } /* DarkOrchid */
            60% { color: #8A2BE2; } /* BlueViolet */
            80% { color: #4B0082; } /* Indigo */
            100% { color: #2E8B57; } /* SeaGreen */
        }
        .changing-color {
            animation: changeColor 30s linear infinite;
            font-size: 48px;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        @import url('https://fonts.googleapis.com/css2?family=Cutive+Mono&display=swap');
        .changing-color {
            font-family: 'Cutive Mono', monospace;
            font-size: 16px;
            color: #0072b1;
            text-align: center;
        }
    </style>
    <div class="changing-color">research and quantitative solutions for defi on solana</div>
''', unsafe_allow_html=True)
    # pairs = ['USDC-SOL', 'SOL-USDC']
    # res2 = {}
    # for pair in pairs:
    #     ffs = sorted(glob(f"../../solana-liquidity-snap/data/jup/{pair}/*.csv"))
    #     res = {}
    #     for ff in ffs:
    #         print(ff)
    #         fnom = os.path.basename(ff).split('-')[0]
    #         df = pd.read_csv(ff, index_col=[0]).T
    #         # st.write(df)
    #         # oA = df['outAmount'].astype(float)
    #         # st.write(df)
    #         df.index = [x for x in range(len(df.index))]
    #         price = df.apply(adjust_by_precision, axis=1).apply(lambda x: x[1]/x[0])
    #         if pair.split('-')[0] == 'USDC':
    #             price = 1/price
    #         res[fnom] = price
    #         print(price)
    #     df = pd.concat(res, axis=1).T
    #     df.index = pd.to_datetime(df.index.astype(int) * 1_000_000_000)
    #     res2[pair] = df
    # dd = pd.concat(res2, axis=0).swaplevel(axis=0)
    # # print(dd)
    # toplt = dd.median(axis=1).unstack().resample('1MIN').last().dropna()
    # st.write(toplt)
    # st.plotly_chart(toplt.plot())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGwzdWloa2o0d2hiaTVlNm1laWVmcGN6NnBwcHJpcjd2YzIwNmE4cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hWKAL74roavpBb75t3/giphy.gif");
            # background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    main()