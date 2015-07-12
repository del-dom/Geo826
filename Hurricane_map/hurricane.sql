--
-- PostgreSQL database dump
--

SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cane; Type: TABLE; Schema: public; Owner: ashton; Tablespace: 
--

CREATE TABLE cane (
    id integer,
    name character varying,
    year integer,
    month integer,
    day integer,
    hour integer,
    max integer,
    press integer,
    lat real,
    lon real
);


ALTER TABLE public.cane OWNER TO ashton;

--
-- Data for Name: cane; Type: TABLE DATA; Schema: public; Owner: ashton
--

COPY cane (id, name, year, month, day, hour, max, press, lat, lon) FROM stdin;
344	GORDON	1994	11	18	0	75	980	33.099998	74.199997
345	GORDON	2000	9	17	6	70	981	26.1	84.900002
346	GRACE	1991	10	29	12	85	982	31.5	63.200001
347	GRACE	1997	10	16	0	40	999	21.200001	64.400002
340	GLADYS	1968	10	20	18	75	966	31.299999	79.699997
341	GLORIA	1985	9	25	6	125	920	25.1	70.900002
342	GLORIA	1979	9	13	12	85	977	35	45
343	GLORIA	1976	10	1	0	90	985	34.700001	56.099998
348	GRACIE	1959	9	29	12	120	950	31.299999	79.599998
349	GRETA	1970	9	27	12	45	1005	24.1	79.800003
298	FOX	1952	10	25	18	130	934	21.799999	81
299	FOX	1951	9	7	12	100	-1	21.700001	50.700001
296	FLOYD	1981	9	8	18	100	975	29.299999	67.800003
297	FLOYD	1999	9	13	12	135	921	23.9	71.400002
294	FLOYD	1987	10	13	18	65	993	24.700001	81.5
295	FLOYD	1993	9	13	0	70	966	48	5
292	FLOSSIE	1978	9	13	0	85	976	31.799999	42.900002
293	FLOSSY	1956	9	24	12	80	-1	29.5	88.699997
290	FLORENCE	1953	9	25	12	110	968	24.4	87.300003
291	FLORENCE	1960	9	19	18	40	-1	20.9	70.199997
199	DOG	1951	9	3	18	100	-1	14.2	62.799999
198	DOG	1950	9	6	6	160	-1	26.700001	68.400002
195	DIANA	1990	8	8	18	85	980	20.9	96.800003
194	DENNIS	1993	8	26	12	45	1000	20	41.400002
197	DIANE	1955	8	13	6	105	969	26.9	60.5
196	DIANA	1984	9	12	0	115	949	33.900002	77.699997
191	DENNIS	1987	9	12	0	45	1000	13.2	29.5
190	DELTA	1972	11	4	0	40	1003	30	49.700001
193	DENNIS	1981	8	21	0	70	995	37.099998	70.400002
192	DENNIS	1999	8	30	6	90	962	32.799999	77.599998
270	FABIAN	1997	9	8	18	40	1005	29.200001	48.799999
271	FAITH	1966	8	29	18	110	957	23.700001	70.900002
272	FAY	2002	9	7	6	50	999	28.1	95.599998
273	FAYE	1975	9	28	18	90	985	37.400002	65
274	FELICE	1970	9	16	0	60	997	29.4	94.099998
275	FELIX	1995	8	13	18	120	929	24.299999	61
276	FELIX	1989	9	6	6	75	979	37.200001	48.099998
277	FELIX	2001	9	14	6	100	962	29.299999	46.599998
278	FERN	1971	9	9	12	80	992	27.1	94.300003
279	FERN	1967	10	3	0	75	987	22.6	93.699997
449	KEITH	2000	10	1	6	120	941	17.9	87.199997
448	KATRINA	1981	11	5	12	75	980	20	80.5
443	KARL	1980	11	27	18	75	985	37.099998	40.5
442	KAREN	1989	12	1	18	50	1000	20.5	83.099998
441	KAREN	2001	10	14	6	70	982	38.599998	63.700001
440	KAREN	1995	8	30	0	45	1002	19	48.200001
447	KATRINA	1999	10	30	0	35	999	13.8	83.400002
446	KATIE	1955	10	17	18	100	984	16.1	72.900002
445	KATE	1985	11	21	0	105	954	26.799999	86.5
444	KARL	1998	9	27	6	90	970	35.5	45.200001
108	BRET	1999	8	22	12	125	944	26.200001	96.099998
109	CAMILLE	1969	8	18	0	165	909	29.4	89.099998
102	BRENDA	1968	6	24	12	65	990	35.599998	59.299999
103	BRENDA	1973	8	21	6	80	-1	19	92.099998
100	BRENDA	1955	8	1	6	60	-1	28.799999	88.800003
101	BRENDA	1960	7	30	0	50	-1	34.599998	78
106	BRET	1993	8	7	12	50	1002	10.8	62.400002
107	BRET	1987	8	21	18	45	1000	15.9	38.400002
104	BRENDA	1964	8	10	18	45	1006	32.900002	60.099998
105	BRET	1981	7	1	18	60	996	36.200001	73.800003
39	ANNA	1961	7	23	0	100	990	15.2	81.400002
38	ANNA	1976	8	2	12	45	-1	42.099998	20.5
33	ANA	1997	7	2	0	40	1000	31.4	72.900002
32	ANA	1991	7	5	0	45	1001	38	57.5
31	ANA	1985	7	19	0	60	996	44.200001	60.299999
30	AMY	1975	7	3	18	60	986	37.299999	64.099998
37	ANITA	1977	9	2	6	150	926	24.200001	97.099998
36	ANDREW	1992	8	24	18	150	922	25.4	75.800003
35	ANDREW	1986	6	8	6	45	1002	36.299999	72.699997
34	ANA	1979	6	22	12	50	1006	14.2	56.900002
438	JULIET	1978	10	11	0	45	1006	26.200001	70.900002
439	KARA	1969	10	18	0	90	-1	43.299999	50.799999
436	JUDITH	1966	9	30	18	45	1007	13.6	59.700001
437	JUDITH	1959	10	20	0	70	-1	30.9	62.900002
434	JOYCE	2000	9	28	12	80	975	11.7	43.799999
435	JUAN	1985	10	29	0	75	973	28.9	92.5
432	JOSEPHINE	1984	10	13	18	90	976	33.700001	71.699997
433	JOSEPHINE	1990	10	6	18	75	980	34.099998	38.400002
430	JOSEPHINE	1996	10	13	6	60	971	53.5	15.5
431	JOSEPHINE	2002	9	19	12	50	1004	41.5	43.299999
339	GLADYS	1975	10	3	18	120	939	37.799999	67
338	GLADYS	1955	9	5	12	80	-1	23.6	96.699997
335	GINGER	1967	10	7	18	45	1002	19.5	18.9
334	GINGER	1971	9	14	0	95	-1	33.299999	53.299999
337	GLADYS	1964	9	18	6	125	951	25.799999	66.5
336	GINNY	1963	10	29	12	95	958	40.799999	67.199997
331	GILBERT	1988	9	14	0	160	888	19.700001	83.800003
330	GERTRUDE	1974	9	30	6	65	1005	11.3	56.400002
333	GILDA	1954	9	26	6	60	-1	15.9	83.5
332	GILDA	1973	10	26	0	60	985	34.099998	70.400002
6	ABLE	1951	5	21	6	100	-1	34.400002	74.699997
99	BONNIE	1992	9	22	6	95	967	37.700001	51.200001
98	BONNIE	1980	8	17	18	85	975	25.799999	39.400002
91	BLANCHE	1969	8	12	18	75	997	35.5	69.900002
90	BILL	1997	7	13	18	65	987	39.599998	58.400002
93	BOB	1985	7	25	0	65	1002	31.6	80.5
92	BLANCHE	1975	7	28	0	75	980	39.299999	67.199997
95	BOB	1991	8	19	6	100	950	36.5	74.5
94	BOB	1979	7	11	12	65	986	29.1	90.599998
97	BONNIE	1998	8	27	18	100	962	33.400002	77.800003
96	BONNIE	1986	6	26	6	75	995	29	93.699997
238	ELENA	1985	9	2	0	110	953	29.4	85.900002
239	ELENA	1965	10	18	12	70	977	39	42.5
234	EDOUARD	1984	9	15	0	55	998	20.299999	95.800003
235	EDOUARD	1996	8	28	0	125	944	20.9	60.400002
236	ELAINE	1974	9	10	12	60	1001	34.799999	69.300003
237	ELENA	1979	9	1	12	35	1008	28.5	95.800003
230	EDNA	1954	9	9	18	105	-1	26.6	75.599998
231	EDNA	1953	9	16	12	110	-1	24.799999	71.099998
232	EDOUARD	1990	8	9	6	40	1003	38.5	29.6
233	EDOUARD	2002	9	3	12	55	1002	30.4	78.400002
1	ABBY	1960	7	11	12	85	-1	14.8	66
146	CINDY	1981	8	5	18	50	1004	41.299999	58.400002
147	CINDY	1959	7	8	12	65	-1	32.299999	78.199997
144	CHRIS	1994	8	20	18	70	980	20.1	54.400002
145	CHRISTINE	1973	9	2	6	60	996	14.9	55.5
142	CHRIS	2000	8	18	12	35	1008	16.200001	55.400002
143	CHRIS	1982	9	11	12	55	994	29.799999	93.800003
140	CHLOE	1967	9	14	18	95	958	28.799999	51.900002
141	CHRIS	1988	8	28	12	45	1005	30.799999	80.800003
148	CINDY	1963	9	17	0	70	996	28	93.900002
149	CINDY	1993	8	16	12	40	1007	17.299999	69.300003
133	CHARLEY	1980	8	24	18	70	990	38	64.699997
132	CHARLEY	1992	9	25	0	95	967	36.099998	33.799999
131	CHARLEY	1998	8	22	6	60	1002	27.5	96.5
130	CHANTAL	1989	8	1	12	70	984	29.5	94.300003
137	CHARLIE	1952	9	26	6	105	-1	28.200001	74.800003
136	CHARLIE	1951	8	20	0	115	-1	20.200001	87.199997
135	CHARLIE	1972	9	22	18	60	944	52	36
134	CHARLEY	1986	8	18	0	70	987	36.5	75.800003
139	CHLOE	1971	8	21	18	55	-1	15.4	67.699997
138	CHARLIE	1950	8	29	12	100	-1	29.200001	58
24	ALMA	1970	5	21	18	70	993	17.200001	81.599998
25	ALMA	1974	8	14	18	55	1007	10	54
26	ALMA	1958	6	15	18	45	-1	22.5	95.599998
27	ALMA	1962	8	29	6	85	-1	40.099998	70.400002
20	ALLISON	1989	6	27	0	45	999	29.700001	95.699997
21	ALLISON	1995	6	5	0	65	988	27.6	86.099998
22	ALLISON	2001	6	6	18	50	1002	28.5	95.300003
23	ALMA	1966	6	9	18	110	970	24.200001	82.400002
28	ALPHA	1972	5	26	12	60	1001	31.6	75.699997
29	AMELIA	1978	7	31	0	45	1005	26.4	97.400002
407	ISIDORE	1984	9	30	0	50	1000	33.599998	76.199997
406	ISBELL	1964	10	15	18	110	968	25.1	82
405	ISABEL	1985	10	10	18	60	1004	28.200001	76.599998
404	ISAAC	1988	10	1	0	40	1005	11.8	57.700001
403	ISAAC	2000	9	29	18	120	943	26.6	54.200001
402	IRMA	1978	10	5	0	45	1001	36.700001	31.200001
401	IRIS	1995	9	1	6	95	965	25.5	58.799999
400	IRIS	2001	10	9	0	125	948	16.5	88
409	ISIDORE	2002	9	23	18	110	935	21.6	88.900002
408	ISIDORE	1996	9	28	6	100	961	16.700001	43.099998
379	HOLLY	1969	9	16	18	75	992	14.5	49.5
378	HILDA	1964	10	2	0	130	942	25.200001	91.400002
371	HELENE	1988	9	24	18	125	938	15.3	46.099998
370	HELENE	1958	9	28	18	115	943	33.900002	77.5
373	HENRI	1979	9	17	12	75	983	20.4	94.300003
372	HELENE	2000	9	25	6	60	986	41.599998	62.200001
375	HERMINE	1980	9	24	6	60	993	18.799999	94.400002
374	HENRI	1985	9	23	12	50	996	36	74.099998
377	HILDA	1955	9	19	18	110	-1	21.799999	95
376	HERMINE	1998	9	20	0	40	999	29	90.900002
393	INGA	1969	10	6	18	100	-1	31.9	59.5
392	INGA	1961	11	7	0	60	1004	19.5	94
88	BEULAH	1959	6	18	18	60	987	23.200001	97.099998
89	BEULAH	1967	9	20	6	140	931	25.1	96.800003
397	IRENE	1971	9	19	18	70	993	11.4	82.300003
396	IRENE	1959	10	8	12	50	1001	30.200001	87.599998
395	IRENE	1999	10	18	6	95	964	34.799999	75.199997
394	IONE	1955	9	18	6	105	-1	28.9	74.699997
82	BETH	1971	8	15	12	75	977	39.700001	67.199997
83	BETSY	1965	9	10	0	135	941	28.299999	89.199997
80	BERYL	1994	8	16	6	50	1003	30.4	85.300003
81	BESS	1978	8	8	0	45	1007	21.1	96.800003
86	BETTY	1972	8	28	0	90	976	40.5	42.599998
87	BEULAH	1963	8	24	6	105	958	23.1	59.599998
84	BETSY	1961	9	6	12	120	945	30.9	56.099998
85	BETSY	1956	8	11	18	105	979	14.4	56
7	AGNES	1972	6	19	12	75	978	28.5	85.699997
245	ELLEN	1973	9	22	12	100	-1	42.099998	45.200001
244	ELLA	1962	10	20	18	100	962	31.299999	73.599998
247	EMILY	1981	9	6	12	80	970	40.799999	58
246	ELOISE	1975	9	23	12	110	955	30.200001	86.300003
241	ELLA	1970	9	12	12	110	967	23.9	97.900002
240	ELLA	1966	7	27	12	45	1012	21.4	63.400002
243	ELLA	1978	9	4	12	120	956	40	63
242	ELLA	1958	9	2	0	100	-1	20	76.300003
249	EMILY	1993	9	1	6	100	962	36.599998	74.400002
248	EMILY	1987	9	23	18	110	958	16.700001	69.099998
458	LAURA	1971	11	21	0	60	997	16.700001	88.199997
459	LAURIE	1969	10	21	12	90	973	26.299999	89.599998
450	KEITH	1988	10	20	18	65	950	52	46
451	KENDRA	1978	10	30	12	70	990	28.9	72.599998
452	KING	1950	10	17	6	105	955	21.9	78.599998
453	KLAUS	1990	10	6	18	70	991	17.4	61.400002
454	KLAUS	1984	11	10	0	80	979	23.799999	57.799999
455	KRISTY	1971	10	21	18	45	992	36.400002	42.900002
456	KYLE	1996	10	12	0	45	1001	16.6	87.5
457	KYLE	2002	9	27	12	75	982	27	60.400002
179	DEBBIE	1969	8	20	12	105	953	25.1	63.299999
178	DEBBIE	1961	9	12	12	105	975	32.200001	45.799999
177	DEAN	1983	9	30	6	55	1009	37	74.900002
176	DEAN	2001	8	28	0	60	995	42.099998	57.5
175	DEAN	1989	8	7	6	90	969	35.599998	64.5
174	DEAN	1995	7	31	0	40	999	29	95
173	DAWN	1972	9	8	12	70	997	36.400002	72.400002
172	DAVID	1979	9	1	18	150	926	17.9	69.699997
171	DANNY	1997	7	19	12	70	984	30.299999	88
170	DANNY	1985	8	15	12	80	988	28.9	92.599998
253	ERIKA	1991	9	11	6	50	998	36.799999	35
182	DEBBY	1988	9	3	0	65	987	20.700001	97.300003
183	DEBBY	1994	9	10	6	60	1006	14.1	61.599998
180	DEBBIE	1957	9	7	6	35	-1	23.9	89.800003
181	DEBBIE	1965	9	29	0	45	1004	28.299999	88.699997
186	DEBRA	1963	9	23	18	65	999	26	48.5
187	DEBRA	1959	7	25	6	75	-1	29.200001	95.099998
184	DEBBY	1982	9	18	0	115	950	38.799999	62.299999
185	DEBBY	2000	8	22	18	75	1004	16.1	58.5
188	DEBRA	1978	8	29	0	50	1000	29.6	93.599998
189	DELIA	1973	9	5	18	60	986	28.4	94
11	ALBERTO	1982	6	4	18	75	985	24	83.599998
10	ALBERTO	1988	8	8	6	35	1006	47	63
13	ALFA	1973	7	31	12	40	-1	37.5	70.800003
12	ALEX	1998	7	31	12	45	1003	15.7	49.200001
15	ALICE	1973	7	4	12	80	990	33.099998	65.099998
14	ALICE	1954	1	3	0	70	-1	17.6	63.200001
17	ALICE	1953	6	6	0	60	997	28.6	85.800003
16	ALICE	1954	6	25	6	70	-1	24.4	96.5
19	ALLEN	1980	8	8	18	165	899	21.799999	86.400002
18	ALICIA	1983	8	18	6	100	963	28.9	95
62	BARRY	1983	8	29	18	70	986	25.4	97.5
322	GEORGES	1998	9	20	6	135	937	16	56.299999
323	GEORGES	1980	9	8	6	70	993	42.900002	55.099998
320	GEORGE	1950	10	4	18	95	-1	33	68
321	GEORGE	1951	9	21	18	50	-1	20.799999	95.199997
326	GERDA	1958	9	15	18	60	1004	17.9	70.599998
327	GERT	1999	9	16	6	130	933	18	51.700001
324	GERDA	1969	9	10	18	110	979	40.099998	69.900002
325	GERDA	1961	10	21	0	60	993	42	65
328	GERT	1993	9	21	18	85	970	21.299999	97
329	GERT	1981	9	12	6	90	990	32.5	68.5
201	DOLLY	1968	8	14	12	70	992	39.799999	51.299999
200	DOG	1952	9	27	0	75	-1	17	54.599998
203	DOLLY	1953	9	10	12	100	995	23.700001	70.5
202	DOLLY	1954	9	1	12	85	-1	29	70.199997
205	DOLLY	1996	8	23	12	70	989	21.6	97.699997
204	DOLLY	2002	8	31	18	50	1000	10.8	37.700001
207	DONNA	1960	9	4	12	140	952	16.799999	59.5
206	DOLLY	1974	9	4	18	45	1005	30.200001	72
209	DORA	1956	9	12	0	60	1004	21.4	96
208	DORA	1964	9	6	6	115	942	26.1	64.400002
77	BERYL	1982	9	1	12	63	998	18.799999	41.700001
76	BERTHA	1996	7	9	12	100	965	21.4	69.400002
75	BERTHA	2002	8	5	6	35	1008	29.6	89.699997
74	BERTHA	1990	8	2	0	70	973	44.200001	60.5
73	BERTHA	1984	9	1	6	35	1007	17	48.700001
72	BERTHA	1957	8	9	12	60	998	28.299999	91.300003
71	BELLE	1976	8	9	6	105	959	32.5	75.199997
70	BECKY	1974	8	30	12	100	977	38	61
79	BERYL	2000	8	15	6	45	1009	24.5	97.699997
78	BERYL	1988	8	9	12	45	1002	30.1	90.400002
2	ABBY	1968	6	4	0	65	994	25.1	83.300003
8	ALBERTO	1994	7	3	12	55	993	29.9	86.699997
68	BECKY	1966	7	3	18	65	986	39.5	53.799999
120	CARRIE	1972	9	4	18	60	993	40.599998	70.199997
121	CELIA	1962	9	13	12	60	995	17.5	52.599998
122	CELIA	1966	7	21	6	70	998	39.5	63.200001
123	CELIA	1970	8	4	18	110	945	27.5	96.300003
124	CESAR	1990	8	5	12	45	1000	25.299999	45.700001
125	CESAR	1984	9	2	18	50	989	46.200001	48.900002
126	CESAR	1996	7	28	6	70	990	12.3	84.199997
127	CHANTAL	1983	9	13	18	65	994	34.400002	55.5
128	CHANTAL	2001	8	21	0	60	1000	18.1	87.699997
129	CHANTAL	1995	7	17	12	60	997	29.299999	69.800003
414	IVAN	1980	10	10	12	90	978	37.799999	39.099998
415	JANET	1955	9	28	0	150	-1	18	86.099998
416	JANICE	1971	9	23	18	55	1005	13.1	48.5
417	JANICE	1958	10	11	6	80	972	38.099998	59
410	ISIDORE	1990	9	7	12	85	978	18.5	37.599998
411	ITEM	1950	10	10	12	95	-1	19.9	95.300003
412	ITEM	1951	10	14	6	70	-1	19.1	81.800003
413	IVAN	1998	9	26	6	80	975	39.200001	36.299999
418	JEANNE	1998	9	25	6	90	973	18	37.200001
419	JEANNE	1980	11	12	0	85	988	24.1	87.400002
319	GAIL	1953	10	4	18	70	-1	14.6	44.200001
318	GABRIELLE	1995	8	12	18	60	990	23.6	97.5
313	FREDERIC	1979	9	13	0	115	946	29.700001	88
312	FRANCES	1976	9	1	6	100	963	26.299999	54.299999
311	FRANCES	1961	10	7	0	110	948	32.900002	66.300003
310	FRANCES	1968	9	28	18	50	1001	34.299999	65.300003
317	GABRIELLE	1989	9	6	0	125	944	22.200001	58.299999
316	GABRIELLE	2001	9	18	18	70	983	36.200001	64.699997
315	FRIEDA	1977	10	18	0	50	1006	17.299999	85
314	FRIEDA	1957	9	25	12	70	992	36.400002	65.199997
3	ABBY	1964	8	8	18	55	1000	28.6	95.199997
368	HEIDI	1971	9	14	0	55	-1	37.099998	69.900002
369	HELENA	1963	10	26	6	45	-1	15.5	60.599998
366	HAZEL	1953	10	9	6	60	-1	25	84.400002
367	HEIDI	1967	10	27	18	80	981	36.200001	46.099998
364	HATTIE	1961	10	31	0	140	920	17.9	86.099998
365	HAZEL	1954	10	15	6	120	-1	30.200001	77.800003
362	HARVEY	1993	9	21	18	65	990	35.599998	55.200001
363	HARVEY	1999	9	22	18	50	999	25.9	81.5
360	HANNAH	1959	10	3	6	110	959	35.099998	65.400002
361	HARVEY	1981	9	15	0	115	946	28.4	62.599998
380	HOLLY	1976	10	25	0	65	995	27.200001	57.5
381	HOPE	1978	9	20	0	55	990	45.5	33
382	HORTENSE	1984	9	26	0	65	993	30.200001	61.099998
383	HORTENSE	1990	8	29	0	55	994	23.5	45.700001
384	HORTENSE	1996	9	13	0	120	935	25.9	71.5
385	HOW	1951	10	4	6	95	-1	33.900002	75.199997
386	HOW	1950	10	2	6	50	-1	26.299999	90.099998
387	HUGO	1989	9	16	18	140	918	14.6	54.599998
388	HUMBERTO	1995	8	25	18	95	968	15.7	43.200001
389	HUMBERTO	2001	9	26	12	90	970	41	59.200001
60	BARBARA	1954	7	29	18	40	-1	28.299999	91.400002
61	BARBARA	1953	8	14	18	95	-1	33.599998	76.300003
258	ERNESTO	1982	10	2	0	60	997	28.5	66.199997
259	ERNESTO	2000	9	3	12	35	1008	19.4	56.599998
64	BARRY	1995	7	8	0	60	997	34	69.599998
65	BARRY	1989	7	12	12	45	1005	22.799999	54.400002
66	BECKY	1970	7	21	12	55	1006	26.6	86.599998
67	BECKY	1962	8	29	18	35	-1	19.5	23.299999
252	ERIKA	1997	9	10	18	110	951	27.9	60.200001
69	BECKY	1958	8	12	12	50	-1	18.9	50
250	EMILY	1999	8	25	0	45	1005	12.1	53.900002
251	EMMY	1976	8	30	12	90	975	34.900002	52
256	ERIN	1989	8	25	12	90	971	39	39.700001
257	ERNESTO	1988	9	5	0	55	994	43.099998	29.700001
254	ERIN	2001	9	10	6	105	969	34.200001	64.099998
255	ERIN	1995	8	3	12	80	974	29.799999	86.599998
469	LOVE	1950	10	19	12	80	-1	26.1	92.199997
468	LORENZO	2001	10	31	6	35	1008	37.400002	43.099998
465	LILI	2002	10	3	0	125	940	26.700001	90.300003
464	LILI	1990	10	13	6	65	992	33.200001	72.5
467	LOIS	1966	11	10	18	70	989	37.299999	36.799999
466	LISA	1998	10	10	18	65	997	47.099998	39.299999
461	LESLIE	2000	10	5	18	60	973	53	10
460	LENNY	1999	11	18	18	135	933	17.4	64.800003
463	LILI	1996	10	19	12	100	960	24.4	74
462	LILI	1984	12	23	18	70	980	24.799999	55.599998
168	DANIELLE	1992	9	26	18	55	1007	37	75.400002
169	DANNY	1991	9	10	12	45	999	15.3	49.700001
164	DAISY	1962	10	7	18	95	968	34.5	67.5
165	DANIELLE	1980	9	6	18	50	1004	29.4	93.400002
166	DANIELLE	1986	9	9	18	50	1002	13	63
167	DANIELLE	1998	9	2	18	90	965	32.900002	70.699997
160	CONNIE	1955	8	10	12	125	970	30.799999	75.300003
161	CORA	1978	8	9	6	80	980	13.9	46.799999
162	CRISTOBAL	2002	8	8	18	45	1008	31	72
163	DAISY	1958	8	29	6	110	970	38	72.900002
9	ALBERTO	2000	8	13	18	110	954	36.799999	53.799999
357	HALLIE	1966	9	21	0	45	997	21.5	95.400002
356	GUSTAV	1990	8	31	6	105	956	30.299999	57.5
355	GUSTAV	1996	8	30	18	40	1005	14.4	38
354	GUSTAV	1984	9	19	6	45	1006	34.599998	62.599998
353	GUSTAV	2002	9	12	18	85	964	40.299999	66.800003
352	GRETA	1978	9	18	6	115	947	15.8	84.300003
351	GRETA	1956	11	5	12	120	970	25.299999	61
350	GRETA	1966	9	5	0	50	1004	20.700001	60.099998
359	HANNA	2002	9	14	12	50	1003	30	88.800003
358	HALLIE	1975	10	27	12	45	1004	35.700001	73.800003
216	DOTTIE	1976	8	20	6	45	996	29.6	80
217	EARL	1998	9	3	18	85	988	28.700001	87.900002
214	DOROTHY	1977	9	29	0	75	980	38.299999	57
215	DOROTHY	1970	8	21	18	60	1002	14.5	60.5
212	DORIS	1975	9	3	12	95	965	41.099998	43
213	DOROTHY	1966	7	28	0	75	-1	39.200001	40.099998
210	DORIA	1971	8	28	18	55	989	34.799999	76.800003
211	DORIA	1967	9	14	18	75	983	37.099998	64.900002
218	EARL	1992	10	2	0	55	990	28	69
219	EARL	1980	9	10	6	65	995	45.200001	36
289	FLORENCE	1988	9	10	0	70	983	28.700001	89.300003
288	FLORENCE	1964	9	8	6	40	-1	22.5	29.9
4	ABLE	1950	8	18	0	120	-1	26.1	73.800003
281	FIFI	1974	9	19	12	95	971	16.1	87.5
280	FIFI	1958	9	7	18	80	-1	17.5	58.299999
283	FLORA	1963	10	4	0	125	944	18	73.099998
282	FLORA	1955	9	9	18	90	972	40.700001	49.700001
285	FLORENCE	1954	9	12	0	65	-1	20.799999	95.900002
284	FLORA	1959	9	12	18	65	994	30.299999	39.799999
287	FLORENCE	2000	9	17	18	70	985	36.099998	61.799999
286	FLORENCE	1994	11	8	6	95	974	39.200001	45.5
263	ETHEL	1964	9	10	18	100	-1	27.700001	63.200001
262	ESTHER	1961	9	20	18	125	950	32	72.599998
261	ESTHER	1957	9	18	12	45	1005	29.200001	90.900002
260	ERNESTO	1994	9	23	6	50	998	13.8	30.5
267	EVELYN	1977	10	16	18	70	999	47.400002	59.200001
266	EVE	1969	8	26	0	50	999	30	75.099998
265	ETHEL	1960	9	15	6	140	-1	28.1	88.900002
264	ETHEL	1956	9	13	0	60	999	27.299999	72.699997
269	FABIAN	1991	10	17	0	40	1009	30	75.5
268	FABIAN	1985	9	19	12	55	994	32.099998	42.5
59	BAKER	1952	9	4	18	105	-1	26.799999	68.400002
58	BAKER	1950	8	21	12	105	-1	16.700001	60
55	AUDREY	1957	6	27	12	125	946	29.299999	93.800003
54	ARTHUR	2002	7	17	0	50	998	44.5	53
57	BAKER	1951	8	3	6	50	-1	24.9	57.5
56	BABE	1977	9	5	6	65	995	28.700001	91.400002
51	ARTHUR	1984	8	30	0	45	1004	12.4	56.299999
50	ARLENE	1987	8	24	18	65	988	48.5	33
53	ARTHUR	1990	7	26	0	60	997	13.7	65
52	ARTHUR	1996	6	23	0	45	996	44	37
63	BARRY	2001	8	6	6	60	991	30.6	86.400002
115	CAROL	1965	9	29	12	85	-1	38.700001	35.400002
114	CARMEN	1974	9	8	0	130	937	28.700001	90.800003
117	CAROL	1953	9	4	18	130	929	19.9	60
116	CAROL	1954	8	28	18	85	-1	29.799999	76.599998
111	CANDY	1968	6	24	0	60	999	28.299999	97.199997
110	CANDICE	1976	8	24	18	80	971	44.400002	51.200001
113	CARLA	1956	9	8	0	45	-1	27.299999	74.300003
112	CARLA	1961	9	11	6	150	936	27.200001	95.699997
119	CARRIE	1957	9	9	12	135	975	18.299999	48.200001
118	CAROLINE	1975	8	31	6	100	963	24.1	97.5
429	JOSE	1999	10	20	12	85	980	16.799999	61.099998
428	JOSE	1981	11	1	18	45	998	31.9	40.799999
421	JENNY	1969	10	3	18	40	1000	25.5	82.099998
420	JENNY	1961	11	7	18	70	974	28.299999	52.299999
423	JERRY	1989	10	16	0	75	983	29.1	95
422	JERRY	2001	10	8	6	45	1004	13.8	62
425	JIG	1950	10	16	18	105	-1	34.200001	58.200001
424	JERRY	1995	8	24	12	35	1004	28.4	81.800003
427	JOAN	1988	10	22	6	125	932	11.9	83.199997
426	JIG	1951	10	16	18	70	-1	30.6	74.800003
308	FRANCES	1998	9	11	0	55	994	27.200001	95.900002
309	FRANCES	1980	9	9	12	100	960	13	31.299999
300	FOX	1950	9	15	18	120	-1	24.6	59.400002
301	FRAN	1990	8	14	12	35	1007	10.2	61.299999
302	FRAN	1984	9	18	12	55	994	20.9	31
303	FRAN	1996	9	5	6	105	952	29.799999	76.699997
304	FRAN	1973	10	12	0	70	993	42.700001	25.799999
305	FRANCELIA	1969	9	3	18	100	973	16.4	86.699997
306	FRANCES	1992	10	25	18	75	976	32.099998	57.400002
307	FRANCES	1986	11	21	18	75	1000	28.5	58.700001
229	EDNA	1968	9	15	6	55	-1	16	35.799999
228	EDITH	1971	9	10	18	140	943	14.8	83.199997
227	EDITH	1967	9	29	0	50	-1	14.6	57
226	EDITH	1963	9	26	18	85	990	14.7	62.700001
225	EDITH	1959	8	18	12	50	-1	15.9	61
224	EDITH	1955	8	28	6	85	-1	27.700001	64.099998
223	EASY	1950	9	4	12	110	-1	27.4	83.199997
222	EASY	1952	10	9	0	95	-1	18.700001	50.5
221	EASY	1951	9	7	12	140	-1	24	66
220	EARL	1986	9	15	12	90	981	29.6	50.099998
391	INEZ	1966	9	29	0	130	929	17.1	68.5
390	ILSA	1958	9	27	0	115	-1	21.4	61.200001
151	CINDY	1987	9	8	12	45	1000	31.1	39.5
150	CINDY	1999	8	29	0	120	944	31.5	58.400002
153	CLAUDETTE	1979	7	25	18	45	1000	29.6	93.900002
152	CLARA	1977	9	9	0	65	998	35.5	64.599998
155	CLAUDETTE	1991	9	7	12	115	946	27.200001	61.700001
154	CLAUDETTE	1997	7	15	12	40	1009	36.200001	69.300003
157	CLEO	1960	8	20	0	80	-1	37.700001	67.800003
156	CLAUDETTE	1985	8	16	18	75	981	36.400002	37
159	CLEO	1958	8	16	0	140	948	19.6	49.799999
158	CLEO	1964	8	24	0	135	950	16.700001	69.5
399	IRIS	1989	9	20	18	60	1001	20	59.200001
398	IRENE	1981	9	29	18	105	960	28.4	56.200001
48	ARLENE	1963	8	10	0	90	969	34.5	61.5
49	ARLENE	1971	7	7	18	55	1000	40.700001	65.900002
46	ARLENE	1967	9	4	18	75	-1	43.299999	52
47	ARLENE	1981	5	9	18	50	1004	23	74.5
44	ARLENE	1999	6	14	18	50	1007	29.1	58.700001
45	ARLENE	1993	6	20	6	35	1001	27	97.199997
42	ANNA	1956	7	27	0	70	1002	21.9	98.400002
43	ARLENE	1959	5	30	12	50	1000	28.4	92
40	ANNA	1965	8	25	18	80	-1	41.099998	48.799999
41	ANNA	1969	7	30	18	60	1003	14.2	46
5	ABLE	1952	8	31	0	90	-1	31.799999	80.5
488	TANYA	1995	11	1	18	75	973	37.099998	43.200001
487	SEBASTIEN	1995	10	23	18	55	1001	21.5	58.5
486	ROXANNE	1995	10	11	0	100	958	20	87
485	PABLO	1995	10	6	12	50	995	12.2	45.799999
484	OPAL	1995	10	4	12	130	919	27.299999	88.5
483	OLGA	2001	11	27	12	80	974	31.5	57.200001
482	NOEL	2001	11	6	18	65	986	38.799999	50.200001
481	NOEL	1995	10	6	18	65	987	32.400002	40.5
480	NICOLE	1998	12	1	0	75	979	35.099998	37.900002
472	MARCO	1990	10	11	6	55	989	26.700001	82.599998
473	MARILYN	1995	9	17	0	100	950	20.4	67
470	LUIS	1995	9	5	6	120	939	17.299999	61
471	MARCO	1996	11	20	12	65	989	14.2	77.800003
476	MICHELLE	2001	11	5	18	120	949	21.5	81.800003
477	MITCH	1998	10	27	0	155	910	17.200001	83.800003
474	MARTHA	1969	11	22	12	80	979	10.3	81
475	MICHAEL	2000	10	20	18	85	965	44	58.5
478	NADINE	2000	10	21	12	50	1000	34.099998	52.299999
479	NANA	1990	10	19	12	75	989	28.5	66.900002
\.


--
-- PostgreSQL database dump complete
--

